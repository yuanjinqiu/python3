import getpass

class people:
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd

    def login(self):
        # self.name = input("user:")
        # self.passwd = input("passwd:")
        if self.name == "jinqiu" and self.passwd == "123456":
            print("login success")
        else:
            print("login faile")

name = input("user:")
pw = getpass.getpass("passwd:")
p1=people(name,pw)
p1.login()