#!/usr/bin/env python3
"""Query TAPD release plans through MCP and write copy-ready update text."""

from __future__ import annotations

import argparse
import ast
import datetime as dt
import json
import os
import re
import subprocess
import sys
import threading
from pathlib import Path
from typing import Any


PROJECTS = {
    "CF": 36787060,
    "MT": 40629242,
}

DEFAULT_FIELDS = "id,name,startdate,enddate,status,description"


class McpClient:
    def __init__(self, command: str, args: list[str], env: dict[str, str] | None = None) -> None:
        process_env = os.environ.copy()
        if env:
            process_env.update(env)

        self._next_id = 1
        self._process = subprocess.Popen(
            [command, *args],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=process_env,
        )
        if self._process.stderr is not None:
            threading.Thread(target=self._drain_stderr, daemon=True).start()

    def _drain_stderr(self) -> None:
        assert self._process.stderr is not None
        for line in self._process.stderr:
            if line.strip():
                print(line.decode("utf-8", errors="replace").rstrip(), file=sys.stderr)

    def close(self) -> None:
        if self._process.poll() is None:
            self._process.terminate()
            try:
                self._process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self._process.kill()

    def initialize(self) -> None:
        self.request(
            "initialize",
            {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "tapd-weekly-release-plan",
                    "version": "0.1.0",
                },
            },
        )
        self.notify("notifications/initialized", {})

    def call_tool(self, name: str, arguments: dict[str, Any]) -> str:
        result = self.request("tools/call", {"name": name, "arguments": arguments})
        if result.get("isError"):
            raise RuntimeError(extract_text(result) or f"MCP tool failed: {name}")
        return extract_text(result)

    def notify(self, method: str, params: dict[str, Any]) -> None:
        self._write_message({"jsonrpc": "2.0", "method": method, "params": params})

    def request(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        request_id = self._next_id
        self._next_id += 1
        self._write_message(
            {
                "jsonrpc": "2.0",
                "id": request_id,
                "method": method,
                "params": params,
            }
        )

        while True:
            message = self._read_message()
            if message.get("id") != request_id:
                continue
            if "error" in message:
                raise RuntimeError(message["error"])
            return message.get("result", {})

    def _write_message(self, message: dict[str, Any]) -> None:
        assert self._process.stdin is not None
        body = json.dumps(message, ensure_ascii=False).encode("utf-8")
        self._process.stdin.write(body + b"\n")
        self._process.stdin.flush()

    def _read_message(self) -> dict[str, Any]:
        assert self._process.stdout is not None
        while True:
            line = self._process.stdout.readline()
            if line == b"":
                raise RuntimeError("MCP server closed stdout")
            line_text = line.decode("utf-8", errors="replace").strip()
            if line_text:
                return json.loads(line_text)


def extract_text(result: dict[str, Any]) -> str:
    content = result.get("content")
    if isinstance(content, list):
        return "\n".join(
            item.get("text", "")
            for item in content
            if isinstance(item, dict) and item.get("type") == "text"
        ).strip()
    if "result" in result:
        return str(result["result"])
    return ""


def load_jsonish(text: str) -> Any:
    text = text.strip()
    if not text:
        return None

    fence_match = re.search(r"```(?:json)?\s*(.*?)```", text, flags=re.S)
    if fence_match:
        text = fence_match.group(1).strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    try:
        return ast.literal_eval(text)
    except (SyntaxError, ValueError):
        return text


def unwrap_items(value: Any, key: str) -> list[dict[str, Any]]:
    value = load_jsonish(value) if isinstance(value, str) else value
    if isinstance(value, dict):
        for container_key in ("data", "result", "items", "list"):
            if container_key in value:
                return unwrap_items(value[container_key], key)
        return [value[key]] if key in value and isinstance(value[key], dict) else [value]
    if isinstance(value, list):
        items: list[dict[str, Any]] = []
        for item in value:
            parsed = load_jsonish(item) if isinstance(item, str) else item
            if isinstance(parsed, dict) and isinstance(parsed.get(key), dict):
                items.append(parsed[key])
            elif isinstance(parsed, dict):
                items.append(parsed)
        return items
    return []


def parse_date(value: Any) -> dt.date | None:
    if not value:
        return None
    match = re.search(r"\d{4}-\d{2}-\d{2}", str(value))
    if not match:
        return None
    try:
        return dt.date.fromisoformat(match.group(0))
    except ValueError:
        return None


def title_dates(name: str, year: int) -> list[dt.date]:
    dates: list[dt.date] = []
    for month, day in re.findall(r"(\d{1,2})月(\d{1,2})日?", name):
        try:
            dates.append(dt.date(year, int(month), int(day)))
        except ValueError:
            continue
    return dates


def week_range(target: dt.date) -> tuple[dt.date, dt.date]:
    start = target - dt.timedelta(days=target.weekday())
    return start, start + dt.timedelta(days=6)


def release_mentions_week(release: dict[str, Any], start: dt.date, end: dt.date) -> bool:
    name = str(release.get("name", ""))
    dates_in_title = title_dates(name, start.year)
    if dates_in_title:
        return any(start <= date <= end for date in dates_in_title)

    release_start = parse_date(release.get("startdate"))
    release_end = parse_date(release.get("enddate")) or release_start
    return bool(release_start and release_end and release_start <= end and release_end >= start)


def load_mcp_server(config_path: Path, server_name: str) -> tuple[str, list[str], dict[str, str]]:
    config = json.loads(config_path.expanduser().read_text(encoding="utf-8"))
    server = config.get("mcpServers", {}).get(server_name)
    if not server:
        raise SystemExit(f"未在 {config_path} 找到 MCP server：{server_name}")
    if "command" not in server:
        raise SystemExit(f"MCP server {server_name} 不是本地 stdio server，脚本无法直接启动")
    return server["command"], server.get("args", []), server.get("env", {})


def resolve_mcp_server(config_path: Path, server_name: str) -> tuple[str, list[str], dict[str, str]]:
    expanded_path = config_path.expanduser()
    if expanded_path.exists():
        return load_mcp_server(expanded_path, server_name)
    return "uvx", ["mcp-server-tapd"], {
        "TAPD_ACCESS_TOKEN": os.environ.get("TAPD_ACCESS_TOKEN", ""),
        "TAPD_API_USER": os.environ.get("TAPD_API_USER", ""),
        "TAPD_API_PASSWORD": os.environ.get("TAPD_API_PASSWORD", ""),
        "TAPD_API_BASE_URL": os.environ.get("TAPD_API_BASE_URL", "https://api.tapd.cn"),
        "TAPD_BASE_URL": os.environ.get("TAPD_BASE_URL", "https://www.tapd.cn"),
        "BOT_URL": os.environ.get("BOT_URL", ""),
    }


def fetch_release_candidates(client: McpClient, workspace_id: int, start: dt.date, end: dt.date) -> list[dict[str, Any]]:
    common_options = {
        "limit": 200,
        "fields": DEFAULT_FIELDS,
    }
    range_text = client.call_tool(
        "get_release_info",
        {
            "workspace_id": workspace_id,
            "options": {
                **common_options,
                "startdate": start.isoformat(),
                "enddate": end.isoformat(),
                "order": "startdate asc",
            },
        },
    )
    candidates = unwrap_items(range_text, "Release")
    filtered = [item for item in candidates if release_mentions_week(item, start, end)]
    if filtered:
        return filtered

    recent_text = client.call_tool(
        "get_release_info",
        {
            "workspace_id": workspace_id,
            "options": {
                **common_options,
                "order": "created desc",
            },
        },
    )
    return [
        item
        for item in unwrap_items(recent_text, "Release")
        if release_mentions_week(item, start, end)
    ]


def fetch_type_map(client: McpClient, workspace_id: int) -> dict[str, str]:
    text = client.call_tool(
        "get_workitem_types",
        {
            "workspace_id": workspace_id,
            "options": {"limit": 200},
        },
    )
    type_map: dict[str, str] = {}
    for item in unwrap_items(text, "WorkitemType"):
        type_id = str(item.get("id", ""))
        english_name = str(item.get("english_name") or item.get("name") or "UNKNOWN").upper()
        if type_id:
            type_map[type_id] = english_name
    return type_map


def fetch_stories(client: McpClient, workspace_id: int, release_id: str) -> list[dict[str, Any]]:
    text = client.call_tool(
        "get_stories_or_tasks",
        {
            "workspace_id": workspace_id,
            "options": {
                "entity_type": "stories",
                "release_id": release_id,
                "limit": 200,
                "fields": "id,name,workitem_type_id,release_id",
            },
        },
    )
    return unwrap_items(text, "Story")


def story_line(index: int, story: dict[str, Any], type_map: dict[str, str]) -> str:
    story_id = re.sub(r"\D", "", str(story.get("id", "")))[-7:]
    title = str(story.get("name", "")).strip()
    type_id = str(story.get("workitem_type_id", ""))
    story_type = type_map.get(type_id, "UNKNOWN")
    return f"{index}、【{story_type}】{story_id} {title}"


def collect_project_story_lines(
    client: McpClient,
    workspace_id: int,
    start: dt.date,
    end: dt.date,
    start_index: int,
) -> tuple[list[str], int]:
    lines: list[str] = []
    index = start_index
    releases = fetch_release_candidates(client, workspace_id, start, end)
    if not releases:
        return lines, index

    type_map = fetch_type_map(client, workspace_id)
    for release in releases:
        stories = fetch_stories(client, workspace_id, str(release.get("id", "")))
        for story in stories:
            lines.append(story_line(index, story, type_map))
            index += 1
    return lines, index


def build_release_plan_text(
    client: McpClient,
    projects: list[tuple[str, int]],
    target_date: dt.date,
) -> str:
    start, end = week_range(target_date)
    lines = [f"{target_date.month}月{target_date.day}日系统更新内容："]
    next_index = 1

    for _, workspace_id in projects:
        project_lines, next_index = collect_project_story_lines(
            client,
            workspace_id,
            start,
            end,
            next_index,
        )
        lines.extend(project_lines)

    if next_index == 1:
        lines.append("未查询到本周发布计划。")

    return "\n".join(lines)


def build_result_payload(
    text: str,
    project: str,
    target_date: dt.date,
) -> dict[str, Any]:
    start, end = week_range(target_date)
    return {
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "query_date": target_date.isoformat(),
        "week_start": start.isoformat(),
        "week_end": end.isoformat(),
        "project": project,
        "source": "tapd",
        "text": text,
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="通过 MCP 查询 TAPD 本周上线计划。")
    parser.add_argument(
        "--project",
        choices=["CF", "MT", "both"],
        default="both",
        help="查询项目，默认 both。",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="按该日期所在自然周查询，格式 YYYY-MM-DD，默认今天。",
    )
    parser.add_argument(
        "--mcp-config",
        default="~/.cursor/mcp.json",
        help="Cursor MCP 配置路径，本地运行时使用。",
    )
    parser.add_argument(
        "--server",
        default="mcp-server-tapd",
        help="MCP server 名称。",
    )
    parser.add_argument(
        "--output-json",
        help="将查询结果写入 JSON 文件，供网页读取。",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        target_date = dt.date.fromisoformat(args.date)
    except ValueError:
        print("--date 必须是 YYYY-MM-DD 格式", file=sys.stderr)
        return 2

    command, command_args, env = resolve_mcp_server(Path(args.mcp_config), args.server)
    projects = list(PROJECTS.items()) if args.project == "both" else [(args.project, PROJECTS[args.project])]

    client = McpClient(command, command_args, env)
    try:
        client.initialize()
        text = build_release_plan_text(client, projects, target_date)
    finally:
        client.close()

    print(text)
    if args.output_json:
        write_json(Path(args.output_json), build_result_payload(text, args.project, target_date))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
