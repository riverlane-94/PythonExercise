'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''

from math import sqrt

num = []  # 设置一个空的列表
n = 0  # 用来统计素数的个数


def is_prime(n):
    """
    判断一个数是否为素数

    :param n: 待判断的整数
    :return: True（是素数）或 False（不是素数）
    """
    # 处理特殊情况
    if n < 2:
        return False  # 小于2的数都不是素数
    if n == 2:
        return True  # 2是唯一的偶数素数
    if n % 2 == 0:
        return False  # 其他偶数都不是素数

    # 只需检查奇数因子，从3开始到sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


for x in range(101, 201):
    if is_prime(x):
        print(f"{x:3d}是素数")
        n = n+1
        num.append(x)
    else:
        pass
print(f"101到200之间共有 {n} 个素数")
