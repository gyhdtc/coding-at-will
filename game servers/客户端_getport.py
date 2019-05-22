import socket
s_handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = socket.getservbyname('http','tcp')
s_handle.connect(('www.gyhdtc.cn', port))
print (port)