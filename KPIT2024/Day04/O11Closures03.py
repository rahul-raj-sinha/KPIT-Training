
def fun1(*args):
    print(args)
    print(*args)

    print("-" * 60)

fun1()
fun1(1)
fun1(1, 2)
fun1(1, 2, 3)
fun1(1, 2, 3, 4)

print("-" * 60)

def sum(x, y):
    return x + y

   


def logDetails(fnc):
    loginfo = "Logging into the service......."

    def helper(*args):
        print(loginfo)
        print(fnc(*args))
        print("-" * 60)

    return helper

sumRef = logDetails(sum)

sumRef(20, 8)

diffRef = logDetails(diff)

diffRef(20, 8)
