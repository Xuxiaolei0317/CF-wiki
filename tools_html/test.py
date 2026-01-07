import json
import pandas as pd
import datetime

# 扁平化嵌套字典的函数
def flatten_dict(d, parent_key="", sep="_"):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):  # 如果值是字典，递归扁平化
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# 读取并处理嵌套 JSON
with open("/Users/xxl/CF-wiki/docs/tools_html/data.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)

# 创建Excel写入器
excel_file = "/Users/xxl/CF-wiki/docs/tools_html/json_to_excel.xlsx"
with pd.ExcelWriter(excel_file, engine='xlsxwriter', engine_kwargs={'options': {'strings_to_urls': False}}) as writer:
    # 处理 nodes 数据
    if "nodes" in json_data and isinstance(json_data["nodes"], list):
        nodes_data = json_data["nodes"]
        if nodes_data:
            flattened_nodes = [flatten_dict(item) for item in nodes_data]
            df_nodes = pd.DataFrame(flattened_nodes)
            df_nodes.to_excel(writer, sheet_name='Nodes', index=False)
            print(f"✅ 节点数据已保存到 'Nodes' sheet (共 {len(df_nodes)} 条记录)")
    
    # 处理 links 数据
    if "links" in json_data and isinstance(json_data["links"], list):
        links_data = json_data["links"]
        if links_data:
            flattened_links = [flatten_dict(item) for item in links_data]
            df_links = pd.DataFrame(flattened_links)
            df_links.to_excel(writer, sheet_name='Links', index=False)
            print(f"✅ 关联数据已保存到 'Links' sheet (共 {len(df_links)} 条记录)")
    
    # 添加元数据信息到单独的sheet
    metadata = {
        "updateTime": json_data.get("updateTime", datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")),
        "version": json_data.get("version", "1.0"),
        "platform": json_data.get("platform", "GitHub Pages"),
        "totalNodes": len(nodes_data) if "nodes" in json_data else 0,
        "totalLinks": len(links_data) if "links" in json_data else 0,
        "exportTime": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    }
    df_metadata = pd.DataFrame([metadata])
    df_metadata.to_excel(writer, sheet_name='Metadata', index=False)
    print(f"✅ 元数据信息已保存到 'Metadata' sheet")

print(f"\n🎉 转换完成！Excel文件已生成：{excel_file}")