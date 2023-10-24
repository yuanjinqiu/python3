from  IPy  import IP
a = input("请输入网段：")
#计算主机位
print(len(IP(a)))
#输出掩码地址
print(IP(a).netmask())
#列出主机
for i in IP(a):
    print(i)

