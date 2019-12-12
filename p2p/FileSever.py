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
# FileServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
FileServer.bind((FileServerIp, FileServerPort))
# 文件向量：长度为5的【String，bool】类型映射，String为 filename，bool类型表示是否获得
G_FileMap = dict()
# 同时统计 文件总数 和 已经发送的文件数
G_FileNum = int(0)
G_FileSend = int(0)
# 想要创建的线程数量
G_MaxThreads = int(2)
# 文件夹
FilePath = "D:\\Github_File\\coding-at-will\\xjysb\\FileServer"

# 创建文件映射
# return int
def obtain_file_list():
    global G_FileMap
    for file in os.listdir(FilePath):
        G_FileMap[file] = False
    print("The files : ", G_FileMap)
    return G_FileMap.__len__()

# 判断文件是否全部发送（要改）
# return bool
def allfile_send():
    res = bool(True)
    with rlock:
        for file in G_FileMap:
            res = res and G_FileMap[file]
    return res

# 启动服务器
def ServerStart():
    FileServer.listen(5)
    return

# 服务器线程
def ServerThread():
    conn, info = FileServer.accept()
    print("Now : ", info)
    # 先发送文件列表，再等待1秒
    conn.send(bytes(str(G_FileMap), encoding="utf-8"))
    time.sleep(1)
    # 发送文件
    SendFile(conn, conn.fileno())
    return

# 分发文件，每个客户端获得的文件数量为 'FileNum/G_NumOfThread'
## 包含两个函数，传文件还有一个函数，这个函数做点准备和善后工作
def SendFile(connect, info):
    global G_FileMap, G_FileSend
    with rlock:
        # 计算本线程发送文件的数量
        if int((G_FileNum - G_FileSend) / G_MaxThreads) == 1:
            temp = int(G_FileNum / G_MaxThreads + G_FileNum % G_MaxThreads)
        else:
            temp = int(G_FileNum / G_MaxThreads)
        # 遍历文件映射，逐个发送文件
        for filename in G_FileMap:
            if G_FileMap[filename] == False and (G_FileSend < G_FileNum and temp > 0):
                print("Send file [", filename, "] ---> ", info)
                # 真实发送文件函数
                Send_File(connect, filename)
                # 发送成功，修改变量
                G_FileMap[filename] = True
                G_FileSend      = G_FileSend + 1
                temp            = temp - 1
            elif not(G_FileMap[filename] == False):
                pass
            else:
                break
    return

# 真实发送文件函数
# return bool
def Send_File(connect, filename):
    # 得到文件的大小,字节
    fileinfo = {
        "filename":filename,
        "filesize":os.path.getsize(str(FilePath + "\\" + filename))
    }
    # 发送文件信息
    connect.send(bytes(str(fileinfo), encoding="utf-8"))
    
    # 真正的传输文件 #
    with open('%s/%s'%(FilePath, filename),'rb') as f:
        data = f.read()
        connect.sendall(data)
    # 真正的传输文件 #
    time.sleep(2)

# 主函数
if __name__ == '__main__':
    # 定义线程列表
    thread_list = []
    # 获取所有文件
    G_FileNum = obtain_file_list()
    # 开启服务器server_start()
    ServerStart()
    # 启动5个线程
    for i in range(G_MaxThreads):
        my_thread = threading.Thread(target = ServerThread)
        thread_list.append(my_thread)
    # 全部启动
    for t in thread_list:
        t.start()
    # 等待所有文件发送
    while not(allfile_send()):
        pass
    # 等待全部线程结束
    for t in thread_list:
        t.join()
    # 最后关闭服务器
    FileServer.close()
    
# END