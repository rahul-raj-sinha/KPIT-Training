
def fun(*args):
    print(args)
    print("-" * 60)

fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4)

print("-" * 60)
def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def outerFun(fnc):
    logInfo = "Logging into the server"

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))
        print("-" * 60)

    return innerFun

inRef = outerFun(sum)
inRef(20, 15)

diffRef = outerFun(diff)
diffRef(80, 55)