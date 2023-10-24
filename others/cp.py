import random



def foo():
    l1 = random.sample(range(1,36),5)
    l2 = random.sample(range(1,13),2)
    l1.sort()
    l2.sort()
    print("红区：%s 蓝区：%s" %(l1,l2))


if __name__ == '__main__':
    num = input("请选择注数：")
    for i in range(int(num)):
        foo()