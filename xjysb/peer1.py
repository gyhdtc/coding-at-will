import time
import socket
import threading
# 维护一些全局变量

# 全局锁
# !!! 对于下面 G_ 开头的全局变量，要读写他们一定要使用锁 !!!
rlock = threading.RLock()
# 文件服务器ip和端号： FileServerIp、FileServerPort
FileServerIp = '127.0.0.1'
FileServerPort = 5000
# 本服务器Ip和Port
MyServerIp = '127.0.0.1'
MyserverPort = 4000
# 同邻节点Peer的Ip和端号：PeerIp、PeerPort
PeerIp = '127,0,0,1'
PeerPort = 4001
# 文件向量：长度为5的【String，bool】类型映射，String为文件名字，bool类型表示是否获得
G_FileMap = {}

MyServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MyClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 判断文件是否全部发送（要改）
def allfile_recv():
    res = bool(True)
    with rlock:
        for file in G_FileMap:
            res = res and G_FileMap[file]
    return res

# 服务器线程
def Server():
    pass

# 客户端线程
def Client():
    pass

if __name__ == '__main__':
    # 先获取文件列表和某个文件

    # 两个线程：MyServer、MyClient
    ## MyServer 等待peer连接，上传文件
    ## MyClient 尝试连接peer，下载文件
    ### 都要相互竞争锁
    ServerThread = threading.Thread(target=Server)
    ClientThread = threading.Thread(target=Client)
    ServerThread.start()
    ClientThread.start()
    while not(allfile_recv()):
        pass
    # 善后
    ServerThread.join()
    ClientThread.join()
    MyServer.close()
    MyClient.close()

# END