import random

# random.random()
print(random.random())#获取的是0-1之间的随机小数
#0-2之间的整数，都包含，闭区间
print(random.randint(0,2))
#0--5之间的奇数，左闭右开区间
print(random.randrange(1,5,2))
lis = ['whw','wanghw','aaa']
#随机从列表中选择
print(random.choice(lis))
#随机选择两个，两次可以是重复的！ ['whw', 'whw']
print(random.choices(lis,k=2))
#随机选2个，没有重复！ ['wanghw', 'aaa']
print(random.sample(lis,k=2))
#变成随机排序的
print(random.shuffle(lis)) # 注意这是个操作！返回的是：None
print(lis)




#生成随机验证码
import string
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.ascii_letters
s4 = string.digits
print(s1)
print(s2)
print(s3)
print(s4)
con = s3+s4
print(con)
y = random.sample(con,6)
yzm = ''.join(y)
print(yzm)
input_yzm = input('请输入你的验证码:')
if input_yzm == yzm:
    print('登录成功')
else:
    print('验证码不正确')




