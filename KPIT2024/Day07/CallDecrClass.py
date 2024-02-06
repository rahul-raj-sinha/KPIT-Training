
class Calc:

    def __init__(self, arg):
        self.arg = arg

    def __call__(self,a, b):
        # print(self.arg(a, b))
        print("Class Decorator Started......")
        res = self.arg(a, b)
        print("Class Decorator Completed......")
        return res

    def test(self, fnc):
        def helper(a, b):
            print("*" * 60)
            print(fnc(a, b))
            print("-" * 60)

        return helper

def test(fnc):
    def helper(a, b):
        print("*" * 60)
        print(fnc(a, b))
        print("-" * 60)
    return helper


@Calc
def fun(x, y):
    return x * y


print(fun(20, 3))

