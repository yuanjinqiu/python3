class People(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s吃饭"%self.name)


p1 = People("jin")
p2 = People("qiu")
print(p1)
print(p2)
p1.eat()
p2.eat()
