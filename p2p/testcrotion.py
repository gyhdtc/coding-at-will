def consum():
    while True:
        num = yield#等待send
        print("consum:", num)

consum = consum()
# 让consum()启动
next(consum)
for num in range(0,10):
    print("product:", num)
    consum.send(num)



    