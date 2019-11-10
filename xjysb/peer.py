import time
import threading
from concurrent.futures import ThreadPoolExecutor


def tell(i):
    print("this is tread {}.".format(i))
    time.sleep(1)
    return [i, threading.get_ident()]   # 必须有返回，通过.result()拿到返回值


def callback(obj): 
    # obj 相当于传过来的future独享，且回调函数必须有这个参数
    result = obj.result()    # 线程函数的返回值
    print(result)


if __name__ == '__main__':
    future = ThreadPoolExecutor(10)
    a = "ddd"
    for i in range(100):
        # 线程运行结束后将future对象传给回调函数callback(obj)
        future.submit(tell, i,).add_done_callback(callback)   
    future.shutdown(wait=True)      # 此函数用于释放异步执行操作后的系统资源。
