import time
import asyncio

def coroutine_example(name):
    print("start ... name:", name)
    x = yield name
    # time.sleep(5)
    print("send :", x)

coro1 = coroutine_example("GYH1")
next(coro1)

coro2 = coroutine_example("GYH2")
next(coro2)

print('send的返回值:', coro1.send(1))
print('send的返回值:', coro2.send(2))