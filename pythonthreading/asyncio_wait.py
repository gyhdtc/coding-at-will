import asyncio

async def coroutine_example(num):
    print('正在执行name:', num)
    # await asyncio.sleep(2)
    res = 1
    for i in range(num - 3, num):
        res = res * i
    print('执行完毕name:', num)
    return res

loop = asyncio.get_event_loop()

tasks = [coroutine_example(i) for i in [4, 7, 10]]
wait_coro = asyncio.wait(tasks)

print("---------------")
loop.run_until_complete(wait_coro)
print("---------------")

for task in tasks:
    print(task.result())

loop.close()