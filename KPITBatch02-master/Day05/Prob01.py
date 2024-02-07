import time

def calctime(fnc):
    def func(x):
        t1 = time.time()
        res = fnc(x)
        t2 = time.time()
        print(f"function executed in {t2-t1}")
    return func

@calctime
def fun(n):
    for i in range(1,n+1):
        continue


fun(100000000)