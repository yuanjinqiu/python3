def input_passwd():
    pwd = input("请输入你的密码：")

    if len(pwd) >= 8:
        return pwd
    e = Exception("密码长度不够")  #抛出异常
    raise e
if __name__ == '__main__':
    try:
        input_passwd()
    except Exception as res:  #调用异常
        print(res)