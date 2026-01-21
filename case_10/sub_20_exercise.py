'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
from numpy.ma.core import append

# 初始条件
sum_height = []  # 用于累积路程

# 循环第1到第10次落地
for i in range(1, 11):
    down_height = 100 * (0.5 ** (i - 1))  # 下落高度
    up_height = 0.5 * down_height  # 反弹高度

    sum_height.append(down_height)  # 记录下落路程

    # 只有前9次反弹后还会继续下落，所以第10次不加反弹
    if i < 10:
        sum_height.append(up_height)

# 计算总路程
total = sum(sum_height)
print(f"第10次落地时共经过 {total:.2f} 米")

# 输出第10次反弹高度
final_bounce = 0.5 * (100 * (0.5 ** 9))
print(f"第10次反弹高度：{final_bounce:.2f} 米")