'''
题目：模拟Linux用户登录。
'''

import time

global user, name

user = {
    'aaa': '123',
}


def login():
    global name
    name = input('Username:')
    pswd = input('Password:')
    if name not in user:
        return False
    return user[name] == pswd


while (not login()):
    time.sleep(3)  # 暂停3秒
    print('Authentication failure')

print(name + '@localhost:~$')
