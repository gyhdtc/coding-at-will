import threading
import time

def traffic_light(event):
    count = 0
    event.set()
    while True:
        # 如果计数器[0, 5)之间， 红灯，event=False
        if 0 <= count < 5:
            event.clear()
            print("light is Red")
        # 如果计数器[5, 10)之间， 绿灯，event=True
        elif 5 <= count < 10:
            event.set()
            print("light is Green")
        # 如果计数器大于10，红灯，将event设置为False，计数器置为0
        else:
            event.clear()
            count = 0
        time.sleep(1)
        count += 1

def car(name, event):
    while True:
        if not event.is_set():
            # event为False, 表示红灯， 车只能等待
            print("RED, the %s is waiting..." % name)
            # 此处会阻塞住，直到event被设置为True在执行
            event.wait()
            print("Green, The %s going...." % name)

e = threading.Event()
light = threading.Thread(target=traffic_light, args=(e,))
light.start()
car1 = threading.Thread(target=car, args=("Tesla", e, ))
car1.start()