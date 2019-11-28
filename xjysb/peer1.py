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
G_FileMap = dict()
# 创建服务器套接字
MyServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# MyServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
MyServer.bind((MyServerIp, MyserverPort))
# 文件保存位置
FilePath = "D:\\Github_File\\coding-at-will\\xjysb\\peer1"

# 判断文件是否全部发送（要改）
# return bool
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
    # 有客户连接，尝试获得锁，因为要修改全局变量、交换文件
    with rlock:
        # copy文件列表，与一会接收到的对比，客户端没有的我有的就上传
        print(connect.getsockname(), info)

# 客户端线程
def Client():
    MyClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MyClient.connect((PeerIp, PeerPort))
    with rlock:
        # copy文件列表，上传到服务器，服务器对比之后会给我没有的文件
        print()

# 从服务器接收文件列表
def RecvFileMap(MyClient):
    global G_FileMap
    # 接收文件映射 From server
    Recv_FileMap = str(MyClient.recv(1024), 'utf-8')
    with rlock:
        G_FileMap = eval(Recv_FileMap)
    print(G_FileMap)
    
# 从服务器接受部分文件
def RecvFile(MyClient):
    # 接收文件信息：文件名、大小
    FileInfo = str(MyClient.recv(1024), 'utf-8')
    while FileInfo:
        print(FileInfo)
        FileInfoMap = eval(FileInfo)
        filename = FileInfoMap['filename']
        filesize = FileInfoMap['filesize']
        
        # 真正的保存文件 #
        with open(r'%s\\%s'%(FilePath, filename),'wb') as f:
            recv_size = 0
            while recv_size < filesize:
                line = MyClient.recv(1024)
                f.write(line)
                recv_size += len(line)
                print('总大小：%s  已下载大小：%s' % (filesize, recv_size))
        # 真正的保存文件 #
        time.sleep(1)
        FileInfo = str(MyClient.recv(1024), 'utf-8')
    # while Recv_File != "":
    #     print(Recv_File)
    #     G_FileMap[Recv_File] = True
    #     Recv_File = str(MyClient.recv(1024), 'utf-8')

if __name__ == '__main__':
    # 先获取文件列表和某个文件，定义
    MyClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MyClient.connect((FileServerIp, FileServerPort))
    RecvFileMap(MyClient)
    RecvFile(MyClient)
    MyClient.close()

    # 两个线程：MyServer、MyClient
    ## MyServer 等待peer连接，上传文件
    ## MyClient 尝试连接peer，下载文件
    ### 都要相互竞争锁
    # ServerThread = threading.Thread(target=Server)
    # ClientThread = threading.Thread(target=Client)
    # ServerThread.start()
    # ClientThread.start()
    # while (allfile_recv()):
    #     pass
    # # 善后
    # ServerThread.join()
    # ClientThread.join()
    # MyServer.close()
    # MyClient.close()

# END