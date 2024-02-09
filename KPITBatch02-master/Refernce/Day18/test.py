
a = 10

def fun():
    global a
    print(a)
    a = 100


fun()
print(a)