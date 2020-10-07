import serial
import threading
import time
from multiprocessing import Process

def read():
    print("read:")
    f = open("testthread.txt","w")
    while True:
        f.write("1 ") 
        time.sleep(1)
    f.close()
    
def write():
    print("write:")
    while True:
        i = 1#input("write : ")
        print(i)
        time.sleep(3)

if __name__ == '__main__':
    process_list = []
    p1 = Process(target=write)
    p2 = Process(target=read)
    p1.start()
    p2.start()
    process_list.append(p1)
    process_list.append(p2)

    for i in process_list:
        i.join()
    
    print("end")