def coroutine_example(name):
    print('start coroutine...name:', name)
    x = yield name #调用next()时，产出yield右边的值后暂停；调用send()时，产出值赋给x，并往下运行
    print('send值:', x)
    return 'zhihuID: Zarten'

def grouper2():
    result2 = yield from coroutine_example('Zarten') #在此处暂停，等待子生成器的返回后继续往下执行
    print('result2的值：', result2)
    return result2

def grouper():
    result = yield from grouper2() #在此处暂停，等待子生成器的返回后继续往下执行
    print('result的值：', result)
    return result

def main():
    g = grouper()
    next(g)
    try:
        g.send(10)
    except StopIteration as e:
        print('返回值：', e.value)

if __name__ == '__main__':
    main()