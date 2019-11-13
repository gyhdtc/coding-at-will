from concurrent.futures import ThreadPoolExecutor
import time

def tell(i):
    print("this is tread {}.".format(i))
    time.sleep(1)

if __name__ == '__main__':
    future = ThreadPoolExecutor(10)
    a = "ddd"
    for i in range(100):
        future.submit(tell, (i,))   # 添加一个线程到线程池
    future.shutdown(wait=True)      # 此函数用于释放异步执行操作后的系统资源。