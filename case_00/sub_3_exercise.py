'''
题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
'''

import math


def main():
    for n in range(-100, 1000):
        root1 = math.isqrt(n + 100)
        root2 = math.isqrt(n + 268)
        if root1 * root1 == n + 100 and root2 * root2 == n + 268:
            print(n)

main()