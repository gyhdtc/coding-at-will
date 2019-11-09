import socket
import string
import threading
import time

def send(server):
    while True:
        data = input('>')
        if data != "exit" and data != "":
            server.send(bytes(data, encoding="utf-8"))
            print ("[send] ", data)
        elif data == "exit":
            server.send(bytes(data, encoding="utf-8"))
            print ("[send] ", data)
            print ("[END]")
            break

def rec(client):
    while True:
        try:
            RecData = str(client.recv(BUFSIZE), "utf-8")
            print("[rec] ", RecData)
            if RecData == "exit":
                print("[END]")
                break
        except:
            break
        
# 用 client 连接
BUFSIZE = 1024
MyServer = socket.socket()
FileServerHost = "127.0.0.1"    # 获取 文件 服务器主机名
FileServerPort = 12345              # 设置 文件 服务器端口号
MyServer.bind((FileServerHost, FileServerPort))

print("waiting for connection...")
MyServer.listen(1)
MyClient, addr = MyServer.accept()
print("...connection from:", addr)

t1 = threading.Thread(target=send, args=(MyClient,))
t1.start()

t2 = threading.Thread(target=rec, args=(MyClient,))
t2.start()

time.sleep(1000)
MyClient.close()
MyServer.close()