# create_project_structure.py - 同级创建文件夹与.ipynb文件
import os
from pathlib import Path

# 定义需要创建的文件夹（与脚本/ipynb同级）
folders = [
    "data_raw",    # 原始数据
    "data_clean",  # 清洗后数据
    "output",      # 输出结果
    "output/tables",
    "output/charts"
]

# 定义需要创建的.ipynb和文档（与文件夹同级）
base_files = [
    "README.md",
    "00_analysis_report.ipynb",
    "01_data_clean.ipynb",
    "02_data_analysis.ipynb"
]

def create_structure():
    # 1. 创建文件夹（同级目录）
    for folder in folders:
        folder_path = Path(folder)
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ 已创建文件夹: {folder_path.absolute()}")
    
    # 2. 创建.ipynb和文档（同级目录）
    for file in base_files:
        file_path = Path(file)
        if not file_path.exists():
            file_path.touch()  # 创建空文件
            print(f"✅ 已创建文件: {file_path.absolute()}")
        else:
            print(f"ℹ️ 文件已存在: {file_path.absolute()}")
    
    # 3. 提示放置原始数据
    print(f"\n📌 请将 'Mfytop15.xlsx' 和 'xfytop15.xlsx' 复制到: {Path('data_raw').absolute()}")

if __name__ == "__main__":
    create_structure()
    print("\n🎉 目录结构创建完成！所有.ipynb文件与文件夹同级存放")