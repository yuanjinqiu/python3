import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',5009))

s.send('hello'.encode("utf-8"))
#接收数据
dt = s.recv(1024)
print(dt)

s.close()



