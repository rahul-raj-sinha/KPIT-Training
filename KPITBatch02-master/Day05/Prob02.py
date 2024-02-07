def dec1(fnc):
    def helper():
        print("-"*60)
        fnc()
        print("#"*60)
    return  helper
def dec2(fnc):
    def helper():
        print("*"*60)
        fnc()
        print("_"* 60)
    return helper
@dec1
@dec2
def fun():
    print("Welcome")
fun()

