import socket

newclient = socket.socket()
#host = "49.123.93.176" # 获取本地主机名
host = socket.gethostname()
port = 12345                # 设置端口号

newclient.connect((host, port))
print (newclient.recv(1024))
newclient.close()