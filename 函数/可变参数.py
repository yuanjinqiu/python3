
def fun(*args,**kwargs):
    print(args)
    print(kwargs)

def fun1(*args,**kwargs):
    print("无参数")

if __name__ == '__main__':
    a = 1
    b = 2
    c = (3,4,5)
    fun(a,b,c,dic=3)
    fun1()



