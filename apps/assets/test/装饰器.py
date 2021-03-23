import time

def outter(aaa):
    print("有参数的装饰器：%s" %aaa)
    def inner(func):

        def timer(*args,**kwargs):

            start = time.time()

            res = func(*args,**kwargs)
            stop = time.time()
            print(stop-start)
            return res

        return timer
    return inner

@outter("xxxxx")
def Test1(test):

    time.sleep(1)
    print("被装饰的函数")
    print(test)

    return test




Test1(111)




list
