import serial
import threading
import time

ser = serial.Serial('com1', 115200, timeout=0.5)
index = 0
i = 0

def loop():
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

t = threading.Thread(target=loop(), name="LoopThread")
t.start()
t.join()