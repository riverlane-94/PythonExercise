'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

# 加一个数字统计
count = 0
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != c and b != c and a != c:
                pass
                count += 1
                print(a, b, c, sep='/')
print(f"共有数字{count}个")
