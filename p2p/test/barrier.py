import time
import threading

bar3 = threading.Barrier(3)  # 创建barrier对象，指定满足3个线程
bar2 = threading.Barrier(2)  # 创建barrier对象，指定满足3个线程
bar1 = threading.Barrier(1)  # 创建barrier对象，指定满足3个线程
def worker1():
    print("worker1")
    time.sleep(2)
    bar1.wait()
    print("worker1")
    bar2.wait()
    bar3.wait()

def worker2():
    print("worker2")
    time.sleep(2)
    bar2.wait()
    print("worker2")
    bar3.wait()

def worker3():
    print("worker3")
    time.sleep(2)
    bar3.wait()
    print("worker3")

thread_list = []
t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)
t3 = threading.Thread(target=worker3)
thread_list.append(t1)
thread_list.append(t2)
thread_list.append(t3)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()