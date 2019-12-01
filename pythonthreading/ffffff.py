import asyncio
import time
from threading import Thread

def start_thread_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def thread_example(name):
    await asyncio.sleep(2)
    print('正在执行name:', name)
    return '返回结果：' + name



new_loop = asyncio.new_event_loop()
t = Thread(target= start_thread_loop, args=(new_loop,))
t.setDaemon(True)
t.start()

future1 = asyncio.run_coroutine_threadsafe(thread_example('Zarten1'), new_loop)

future2 = asyncio.run_coroutine_threadsafe(thread_example('Zarten2'), new_loop)

print('主线程不会阻塞')

future3 = asyncio.run_coroutine_threadsafe(thread_example('Zarten3'), new_loop)

print('继续运行中...')

while 1:
    print("1")
    time.sleep(1)