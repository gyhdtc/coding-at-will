import time
import threading

bar1 = threading.Barrier(2)  # 创建barrier对象，指定满足3个线程
bar2 = threading.Barrier(2)  # 创建barrier对象，指定满足2个线程

def worker1():
    print("worker 1")
    bar1.wait()

def worker2():
    bar1.wait()
    print("worker 2")
    bar2.wait()

def worker3():
    bar2.wait()
    print("worker 3")


thread_list = []
t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)
t3 = threading.Thread(target=worker3)
thread_list.append(t1)
thread_list.append(t2)
thread_list.append(t3)

for t in thread_list:
    t.start()