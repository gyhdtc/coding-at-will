import threading
import time

condition = threading.Condition()    # 创建condition对象

def func():
    condition.acquire()    # 如果没有with语句，必写这句，否者报错
    condition.wait()       # 阻塞，等待其他线程调用notify()
    print("in func..")
    condition.release()    # 与acquire()成对出现

# 启10个线程
for i in range(10):
    t = threading.Thread(target=func, args=())
    t.start()

time.sleep(5)

condition.acquire()
condition.notify(2)        # 通知两个线程执行
condition.release()