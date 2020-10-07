import serial
import threading
import time

ser = serial.Serial('com1', 115200, timeout=0.5)
index = 0
i = 0

def read():
    global i
    print("串口状态:" + str(ser.is_open))
    f = open("test.txt","w")
    while ser.isOpen():
        if (ser.in_waiting > 0):
            buffer = ser.read(2)
            #i = len(buffer)
            #p = ProcMsg(buffer)
            #buffer.decode('gbk')
            #print(i)
            x = buffer[0] + buffer[1]*256
            print(x)
            i = i + 1
            f.write(str(x)+"\n") 
            #p.proc()
        elif (ser.in_waiting <= 0):
            time.sleep(1)
    f.close()
def write():
    global i
    while True:
        print("串口状态:" + str(ser.is_open))
        a = [[1,4,40000,40000,40000,40000,40000,2], 
        [1,3,0,0,0,0,0,2], 
        [1,5,0,0,0,0,0,2], 
        [1,7,46861,23560,35278,36667,22108,2], 
        [1,7,20000,20000,20000,20000,20000,2]]
        h = input("command : ")
        for x in a[int(h)-1]:
            num1 = int.to_bytes(x,2,byteorder="little")
            ser.write(num1)
            print("done")
        
t1 = threading.Thread(target=write(), name="writeThread")
t2 = threading.Thread(target=read(), name="readThread")
t1.start()
t2.start()
t1.join()
t2.join()