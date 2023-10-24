import socket

host = "www.baidu.com"
ports = [80, 443, 8080]

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.error:
        print(f"Error connecting to port {port}")
