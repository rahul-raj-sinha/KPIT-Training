
def outerFun(greet):

    # simple Curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun

outerFun("Hello")("Sachin")

EngGrt = outerFun("Hello")
HndGrt = outerFun("Namaskar")
TmlGrt = outerFun("Vanakam")

EngGrt("Rahul")
HndGrt("Shami")
TmlGrt("Natrajan")