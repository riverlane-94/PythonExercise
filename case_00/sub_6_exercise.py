'''
题目：斐波那契数列。
'''

def fe(x):
    a = 0
    b = 1
    for i in range(x):

        a,b = b,a+b
    print(a)

fe(10)