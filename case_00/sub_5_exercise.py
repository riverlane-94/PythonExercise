'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''
user_input = input("请输入三个数：")

# 用 split() 切开
parts = user_input.split()

print(parts)  # ['3', '1', '2']
print(type(parts))  # <class 'list'>