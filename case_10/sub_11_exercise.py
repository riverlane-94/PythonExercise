# 推荐写法：使用 f-string
f1, f2 = 1, 1
for i in range(1, 22):
    RED = '\033[91m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'

    print(f"{RED}{f1:12d}{ENDC} {GREEN}{f2:12d}{ENDC}", end='')
    if (i % 3) == 0:
        print()

    # 更新斐波那契数列
    next_fib = f1 + f2
    f1 = f2
    f2 = next_fib