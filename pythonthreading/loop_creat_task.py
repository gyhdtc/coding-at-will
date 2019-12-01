import asyncio

async def coroutine_example():
    await asyncio.sleep(1)
    print('zhihu ID: Zarten')
# 函数变量
coro = coroutine_example()
# 事件循环
loop = asyncio.get_event_loop()
# 多个任务
task = loop.create_task(coro)
print('运行情况：', task)
#　阻塞调用，直到协程运行结束才返回。
#　参数是future，传入协程对象时内部会自动变为future。
loop.run_until_complete(task)
print('再看下运行情况：', task)
loop.close()