'''
题目：打印出所有的"水仙花数"
'''

"""
题目：打印出所有的"水仙花数"
"""

print("所有水仙花数如下：")

# 遍历所有三位数
for num in range(100, 1000):
    # 分离各位数字
    hundred = num // 100        # 百位
    ten = (num // 10) % 10      # 十位
    unit = num % 10             # 个位

    # 计算立方和
    sum_of_cubes = hundred**3 + ten**3 + unit**3

    # 判断是否为水仙花数
    if sum_of_cubes == num:
        print(f"{num} 是水仙花数")