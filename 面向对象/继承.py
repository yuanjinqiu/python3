

class people:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getage(self):
        print(self.age)

class p(people):

    def getname(self):
        print(self.name)


p1 = p("jin",19)

p1.getname()