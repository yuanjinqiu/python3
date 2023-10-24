import subprocess


#单主机
# host = "www.baidu.com"
#
# result = subprocess.call(['ping', '-c', '1', host])
# if result == 0:
#     print("Host is reachable.")
# else:
#     print("Host is unreachable.")

#多主机

with open('ip.txt','r')as f:
    file = f.readlines()
    print(file)
    for ip in file:
        result = subprocess.call(['ping', '-c', '1', ip])
        if result == 0:
            print("%s is reachable" %ip.strip('\n'))
        else:
            print("%s is unreachable" %(ip.strip('\n')))