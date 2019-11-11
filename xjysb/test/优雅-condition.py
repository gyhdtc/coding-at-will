'''
频繁写acquire() / release()很繁琐，下面是优雅的写法
'''
import threading
import time

condition = threading.Condition()    # 创建condition对象

def func(n):
    with condition:            # with更优雅
        condition.wait()       # 阻塞，等待其他线程调用notify()
        print("in func..", n)


# 启10个线程
for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    t.start()

time.sleep(5)

with condition:
    condition.notify_all()        # 通知所有线程执行