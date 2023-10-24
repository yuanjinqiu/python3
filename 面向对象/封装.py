
class people:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def info(self):
        print("my name is: %s" %(self.name))
        print("my age is: %s" %(self.__age))

p = people('jin',18)
p.info()










