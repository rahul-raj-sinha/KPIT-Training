
def outerFun(greet):
    # simple Curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun

KanGrt = outerFun("Namaskara")
EngGrt = outerFun("Good Morning")

KanGrt("Anil")
EngGrt("Sachin")