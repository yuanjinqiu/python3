def demo1():
    return int(input("num is: "))

def demo2():
    return demo1()


if __name__ == '__main__':
    try:
        print(demo2())
    except Exception as res:
        print("未知错误：%s" %res)
