'''
题目：输入某年某月某日（yyyy-MM-dd），判断这一天是这一年的第几天？
'''
from datetime import datetime

# 1. 接收用户输入
date_str = input("请输入日期（格式：yyyy-MM-dd）：")

try:
    # 2. 将字符串转换为 datetime 对象
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # 3. 获取该年第一天的日期
    start_of_year = datetime(date_obj.year, 1, 1)

    # 4. 计算间隔天数并加 1（因为第一天是第1天）
    day_of_year = (date_obj - start_of_year).days + 1

    # 5. 输出结果
    print(f"{date_str} 是这一年中的第 {day_of_year} 天。")

except ValueError as e:
    print("❌ 输入格式错误！请使用 'yyyy-MM-dd' 格式，例如：2026-01-18")

