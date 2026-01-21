"""
函数：输出“今天是星期几”
功能：自动获取当前日期，并打印“今天是星期X”

Author: 骆昊（改编）
Version: 1.0
"""

from datetime import datetime

def show_today_weekday():
    """
    输出“今天是星期几”的中文信息
    例如：今天是星期一
    """
    # 获取当前时间
    now = datetime.now()

    # 映射数字到中文星期
    weekdays = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]

    # 获取今天是星期几（0=星期日，1=星期一，...，6=星期六）
    today_index = now.weekday()

    # 输出结果
    print(f"中午 {weekdays[today_index]}")

# 运行函数
if __name__ == "__main__":
    show_today_weekday()
