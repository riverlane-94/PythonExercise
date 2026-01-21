# 模拟用户数据库（真实系统中应使用文件或数据库）
users = {
    "admin": "123456",
    "alice": "password123",
    "bob": "secret789",
    "charlie": "qwerty"
}

MAX_ATTEMPTS = 3  # 最大尝试次数

def login():
    """用户登录主函数"""
    print("=" * 40)
    print("       欢迎使用 Linux 登录系统")
    print("=" * 40)

    while True:
        username = input("\n请输入用户名: ").strip()
        if not username:
            print("❌ 用户名不能为空，请重新输入。")
            continue

        # 检查用户是否存在
        if username not in users:
            print("❌ 用户名不存在，请重试。")
            continue

        # 开始密码尝试
        attempts = 0
        while attempts < MAX_ATTEMPTS:
            password = input("请输入密码: ").strip()
            if not password:
                print("❌ 密码不能为空。")
                continue

            if password == users[username]:
                print(f"\n✅ 登录成功！欢迎，{username}！")
                print(f"📅 当前时间：{__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                return  # 成功登录，退出函数

            else:
                attempts += 1
                remaining = MAX_ATTEMPTS - attempts
                if remaining > 0:
                    print(f"❌ 密码错误！还有 {remaining} 次机会。")
                else:
                    print(f"❌ 密码连续错误 {MAX_ATTEMPTS} 次，账户已锁定！")
                    print("🔒 请稍后再试或联系管理员。")
                    return  # 账户锁定，退出

        # 如果循环结束仍未登录成功（理论上不会发生）
        print("⚠️ 系统异常，无法继续登录。")

def main():
    """主程序入口"""
    while True:
        choice = input("\n是否要登录？(y/n): ").strip().lower()
        if choice in ['y', 'yes', '是']:
            login()
        elif choice in ['n', 'no', '否']:
            print("👋 感谢使用，再见！")
            break
        else:
            print("❌ 请输入 y 或 n。")

# 启动程序
if __name__ == "__main__":
    main()