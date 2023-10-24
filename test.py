

import random
def sum():
  for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(j,i,i*j),end=' ')
    print()
sum()



import string
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
print(s1)
print(s2)