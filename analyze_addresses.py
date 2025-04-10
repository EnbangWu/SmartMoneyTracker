import pandas as pd
import os
from collections import defaultdict

# 设置数据目录
DATA_DIR = "data"

def load_all_wallets(file_path):
    """读取 CSV 文件，返回所有 Wallet 地址"""
    df = pd.read_csv(file_path)
    return set(df["Wallet"].tolist())

def find_frequent_wallets(file_paths, min_appearances=2):
    """找出至少出现在 min_appearances 个文件中的 Wallet 地址"""
    # 统计每个 Wallet 地址出现在哪些文件中
    wallet_files = defaultdict(list)
    
    # 遍历每个文件，记录 Wallet 地址
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        wallets = load_all_wallets(file_path)
        for wallet in wallets:
            wallet_files[wallet].append(file_name)
    
    # 筛选出至少出现 min_appearances 次的 Wallet 地址
    frequent_wallets = {
        wallet: files for wallet, files in wallet_files.items()
        if len(files) >= min_appearances
    }
    
    # 转换为 DataFrame 格式，按出现次数降序排序
    result = []
    for wallet, files in frequent_wallets.items():
        result.append({"Wallet Address": wallet, "Number of Coins": len(files)})
    
    df = pd.DataFrame(result)
    # 按 Number of Coins 降序排序
    df = df.sort_values(by="Number of Coins", ascending=False)
    return df

def print_grouped_stats(df):
    """按 Number of Coins 分组统计并打印"""
    if df.empty:
        print("没有 Wallet 地址在多个文件中重复出现！")
        return
    
    # 按 Number of Coins 分组并计数
    grouped = df.groupby("Number of Coins").size().to_dict()
    
    # 计算总地址数量
    total_addresses = len(df)
    print(f"\n至少买入 2 个代币的 Wallet 地址总数：{total_addresses}")
    print("按买入代币数量分组：")
    for num_coins, count in sorted(grouped.items(), reverse=True):
        print(f"买入 {num_coins} 个代币的地址有 {count} 个")

def main():
    # 获取所有 CSV 文件路径
    file_paths = [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
    
    if not file_paths:
        print("数据目录中没有 CSV 文件！")
        return
    
    # 找出至少出现 2 次的 Wallet 地址
    result_df = find_frequent_wallets(file_paths, min_appearances=2)
    
    # 打印分组统计信息
    print_grouped_stats(result_df)
    
    if result_df.empty:
        return
    
    # 输出结果到 CSV 文件
    output_file = "smart_money.csv"
    result_df.to_csv(output_file, index=False)
    print(f"\n结果已保存到 {output_file}")
    
    # 在终端打印详细结果
    print("\n详细地址列表：")
    print(result_df)

if __name__ == "__main__":
    main()