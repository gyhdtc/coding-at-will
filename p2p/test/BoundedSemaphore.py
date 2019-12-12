import threading
import time

def func(n):
    # semaphore.acquire()
    with semaphore:
        time.sleep(2)
        print("Thread::", n)
    # semaphore.release()

semaphore = threading.BoundedSemaphore(5)   # 信号量, 每次释放5个线程

thread_list = []
for i in range(23):
    t = threading.Thread(target=func, args=(i,))
    thread_list.append(t)
    t.start()

for j in thread_list:
    j.join()

print("all threads done")