from random import choice
import string



def GenPassword(length=0, chars=string.ascii_letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])


if __name__ == "__main__":
    # 生成10个随机密码


    while True:
        try:
            length = int(input('请输入密码长度'))
        except Exception as e:
            print('请输入整数长度')

        password = GenPassword(length)
        print(password)



