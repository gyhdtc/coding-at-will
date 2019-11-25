import os
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
# 创建套接字，并绑定
FileServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
FileServer.bind((FileServerIp, FileServerPort))
# 文件向量：长度为5的【String，bool】类型映射，String为文件名字，bool类型表示是否获得
G_FileMap = {}
# 同时统计 文件总数 和 已经发送的文件数
G_FileNum = int(0)
G_FileSend = int(0)

# 创建文件映射
def obtain_file_list():
    FilePath = str("D:\\Github_File\\coding-at-will\\xjysb\\FileServer")
    for file in os.listdir(FilePath):
        G_FileMap[file] = False
    print("The number of files : ", G_FileMap.__len__(), G_FileMap)
    return G_FileMap.__len__()

# 分发文件，每个客户端获得的文件数量为 'FileNum/5'
def Handle(connet, info):
    global G_FileMap, G_FileSend
    temp = int(G_FileNum/5)
    # 发送 FileNum/5 个文件
    print("Now : ", conn.getsockname(), info)
    with rlock:
        for file in G_FileMap:
            if G_FileMap[file] == False and (G_FileSend < G_FileNum and temp > 0):
                print("Send file [", file, "] ---> ", info)
                G_FileMap[file] = True
                G_FileSend += 1
                temp -= 1
            elif not(G_FileMap[file] == False):
                pass
            else:
                break

# 判断文件是否全部发送（要改）
def allfile_send():
    res = bool(True)
    with rlock:
        for file in G_FileMap:
            res = res and G_FileMap[file]
    return res

# 启动服务器
def server_start():
    FileServer.listen(5)

# 主函数
if __name__ == '__main__':
    # 获取所有文件
    G_FileNum = obtain_file_list()
    # 开启服务器server_start()
    server_start()
    while not(allfile_send()):
        conn, info = FileServer.accept()
        Handle(conn, conn.fileno())
        # 为每一个连接启动线程
        # mythread = threading.Thread(target = Handle, args=(conn, conn.fileno()))
        # mythread.setDaemon(True)
        # mythread.start()
    # 所有文件分发出去就关闭服务器
    FileServer.close()

# END