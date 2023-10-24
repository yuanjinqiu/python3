import socket

Host = '127.0.0.1'
Port = 5009

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#绑定地址
s.bind((Host,Port))

s.listen(1)
print('staring')

conn,client_addr = s.accept()
#接收数据
data = conn.recv(1024)
print(data)
#发送数据
conn.send(data.upper())
conn.close()
s.close()







