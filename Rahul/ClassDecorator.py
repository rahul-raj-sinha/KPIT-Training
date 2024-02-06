
class Calc(object):
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, a, b):
        print("class decorator started.......")
        res = self.arg(a, b)
        print("class decorator started.......")
        return res

@Calc
def fun(x, y):
    return x * y

print(fun(10, 20))

