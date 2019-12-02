import asyncio
import time

async def coroutine_example1():
    await asyncio.sleep(1)
    return 'zhihu ID: 1'

async def coroutine_example2():
    await asyncio.sleep(10)
    return 'zhihu ID: 2'

coro1 = coroutine_example1()
coro2 = coroutine_example2()

loop = asyncio.get_event_loop()
task1 = loop.create_task(coro1)
task2 = loop.create_task(coro2)

print("1-------------------")
print('1 2 运行情况：', task1, task2)
print("2-------------------")
try:
    print('1 返回值：', task1.result())
    print('2 返回值：', task2.result())
except asyncio.InvalidStateError:
    print('task 1 2状态未完成，捕获了 InvalidStateError 异常')
print("3-------------------")
loop.run_until_complete(task1)
print("3-------------------")
loop.run_until_complete(task2)
print('再看下运行情况：', task1)
print("4-------------------")
print('返回值：', task1.result())
print("5-------------------")
loop.close()