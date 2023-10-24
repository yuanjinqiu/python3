import random

def redboo():
    l=[]
    for i in range(1,36):
        if i < 10:
           num = "0"+ str(i)
           l.append(num)
        else:
           l.append(i)
    red = []
    for j in range(5):
        red.append(random.choice(l))
    return red

def blueboo():
    ll=[]
    for i in range(1,13):
        if i < 10:
           num = "0"+ str(i)
           ll.append(num)
        else:
           ll.append(i)
    blue=[]
    for j in range(2):
        blue.append(random.choice(ll))
    return blue
for k in range(5):
    print(redboo(),blueboo())