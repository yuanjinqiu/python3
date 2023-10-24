

class animal(object):
    def __init__(self,name):
        self.name = name
    def func(self):
        print("%s 动物会叫" %self.name)

class Cat(animal):
    def func(self):
        print("喵喵喵")

class Dog(animal):

    def func(self):
        super().func() #如果要使用父类方法，使用super()函数
        print("%s:汪汪汪" %(self.name))


d1 = Dog("旺财")
d1.func()




