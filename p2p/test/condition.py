import threading
import time

condition = threading.Condition()    # 创建condition对象

def func(i):
    print("in func..", i)
    condition.acquire()    # 如果没有with语句，必写这句，否者报错
    condition.wait()       # 阻塞，等待其他线程调用notify()
    print("in func..", i)
    condition.release()    # 与acquire()成对出现

# 启10个线程
for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    t.start()

time.sleep(5)

condition.acquire()
condition.notify(10)        # 通知两个线程执行
time.sleep(10) #果然验证了finally中的阻塞说法
condition.release()