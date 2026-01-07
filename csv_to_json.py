import csv
import json
import datetime

# 读取 CSV 文件并转换为字典列表
def read_csv_to_dict(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 转换数据类型
            for key, value in row.items():
                if value == '':
                    row[key] = None  # 将空字符串转换为 None
                elif key in ['id', 'source', 'target', 'index']:
                    row[key] = int(value)  # 转换为整数
                elif key in ['x', 'y', 'vx', 'vy']:
                    row[key] = float(value)  # 转换为浮点数
            data.append(row)
    return data

# 主函数
def csv_to_json():
    # 读取两个 CSV 文件
    nodes_data = read_csv_to_dict('/Users/xxl/CF-wiki/nodes_output.csv')
    links_data = read_csv_to_dict('/Users/xxl/CF-wiki/links_output.csv')
    
    # 创建与原始 JSON 结构相同的字典
    result = {
        "nodes": nodes_data,
        "links": links_data,
        "updateTime": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),  # 当前时间
        "version": "1.0",
        "platform": "GitHub Pages"
    }
    
    # 写入 JSON 文件
    with open('/Users/xxl/CF-wiki/docs/tools_html/reconstructed_data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print("✅ CSV 转 JSON 完成！")
    print(f"节点数据：{len(nodes_data)} 条")
    print(f"关联数据：{len(links_data)} 条")
    print(f"输出文件：/Users/xxl/CF-wiki/docs/tools_html/reconstructed_data.json")

# 执行转换
if __name__ == "__main__":
    csv_to_json()
