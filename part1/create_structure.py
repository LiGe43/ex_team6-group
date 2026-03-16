import os
import json

# 1. 定义配置变量
PROJECT_NAME = "ex_team6-group"  # 可修改的主文件夹名

# 2. 定义目录结构
folders = ["data_raw", "data_clean", "output"]

# 3. 定义 notebook 文件
notebooks = [
    "00_analysis_report.ipynb",
    "01_data_clean.ipynb", 
    "02_data_analysis.ipynb"
]

# 4. 创建函数：创建目录
def create_folders(root_path, folder_list):
    for folder in folder_list:
        folder_path = os.path.join(root_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"创建文件夹: {folder_path}")

# 5. 创建函数：生成空 notebook 模板
def create_notebook(filename):
    return {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

# 6. 创建函数：生成 README.md
def create_readme():
    return """# 数据集描述

## 项目概述
本项目用于数据分析任务。

## 数据说明
- **原始数据 (data_raw/)**: 存储下载的原始数据
- **清洗后数据 (data_clean/)**: 存储清洗后的数据

## 输出结果
- 图形和表格保存在 `output/` 目录

## 文件说明
- `00_analysis_report.ipynb`: 总报告
- `01_data_clean.ipynb`: 数据清洗
- `02_data_analysis.ipynb`: 数据分析
"""

# 7. 根目录（仓库目录）- 脚本在 part1 文件夹内，需要取上级目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 8. 定义根目录下的文件
files = {
    "README.md": lambda: create_readme(),
    "00_analysis_report.ipynb": lambda: json.dumps(create_notebook("00_analysis_report.ipynb"), ensure_ascii=False, indent=2),
    "01_data_clean.ipynb": lambda: json.dumps(create_notebook("01_data_clean.ipynb"), ensure_ascii=False, indent=2),
    "02_data_analysis.ipynb": lambda: json.dumps(create_notebook("02_data_analysis.ipynb"), ensure_ascii=False, indent=2),
}

# 9. 主程序执行流程
if __name__ == "__main__":
    print(f"项目根目录: {ROOT_DIR}")
    
    # 1. 创建子文件夹
    print("\n=== 创建子文件夹 ===")
    create_folders(ROOT_DIR, folders)
    
    # 2. 创建文件
    print("\n=== 创建文件 ===")
    for filename, content_func in files.items():
        file_path = os.path.join(ROOT_DIR, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_func())
        print(f"创建文件: {file_path}")
    
    print("\n项目结构创建完成！")
