import json
import time
import socket
import threading
# 维护一些全局变量

# 全局锁
# !!! 对于下面 G_ 开头的全局变量，要读写他们一定要使用锁 !!!
rlock = threading.RLock()
# 文件服务器ip和端号： FileServerIp、FileServerPort
FileServerIp = '127.0.0.1'
FileServerPort = int(5000)
# 本服务器Ip和Port
MyServerIp = '127.0.0.1'
MyserverPort = int(8000)
# 同邻节点Peer的Ip和端号：PeerIp、PeerPort
PeerIp = '127.0.0.1'
PeerPort = int(8001)
# 文件向量：长度为5的【String，bool】类型映射，String为文件名字，bool类型表示是否获得
G_FileMap = {}
# 创建服务器套接字
MyServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# MyServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
MyServer.bind((MyServerIp, MyserverPort))

# 判断文件是否全部发送（要改）
def allfile_recv():
    res = bool(True)
    with rlock:
        for file in G_FileMap:
            res = res and G_FileMap[file]
    return res

# 服务器线程
def Server():
    MyServer.listen(1)
    connect, info = MyServer.accept()
    with rlock:
        pass

# 客户端线程
def Client():
    pass

# 从服务器接收
def RecvFileList():
    global G_FileMap
    RecvData = str(MyClient.recv(1024),'utf-8')
    with rlock:
        G_FileMap = eval(RecvData)
    print(G_FileMap)

if __name__ == '__main__':
    # 先获取文件列表和某个文件，定义
    MyClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MyClient.connect((FileServerIp, FileServerPort))
    RecvFileList()
    time.sleep(5)
    MyClient.close()

    # 两个线程：MyServer、MyClient
    ## MyServer 等待peer连接，上传文件
    ## MyClient 尝试连接peer，下载文件
    ### 都要相互竞争锁
    ServerThread = threading.Thread(target=Server)
    ClientThread = threading.Thread(target=Client)
    ServerThread.start()
    ClientThread.start()
    while (allfile_recv()):
        pass
    # 善后
    ServerThread.join()
    ClientThread.join()
    MyServer.close()
    MyClient.close()

# END