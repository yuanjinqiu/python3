

class People(object):
    def __new__(cls, *args, **kwargs):
        print("分配空间")
        res = super().__new__(cls)
        return res

    def __init__(self):
        print("一个人")

p = People()
print(p)


























