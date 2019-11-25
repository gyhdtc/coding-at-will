import time
import socket
import threading

# 每一个Peer都应该维护一些全局变量
## 文件向量：长度为5的【String，bool】类型映射，String为文件名字，bool类型表示是否获得
## 文件服务器ip和端号： FileServerIp、FileServerPort
## 同邻节点Peer的Ip和端号：PeerIp、PeerPort
FileServerIp = '127.0.0.1'
FileServerPort = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect((FileServerIp, FileServerPort))

#if __name__ == '__main__':
    # 两个线程：MyServer、MyClient
    ## 客户端线程：首先输入文件服务器ip和端号 FileServerIp、FileServerPort 和 邻居ip和端口 PeerIp、PeerPort。
    ### 然后：连接FileServer，获得一些文件；断开连接；两个线程竞争锁，服务器被连接之后获得锁、客户端连接之后获得锁