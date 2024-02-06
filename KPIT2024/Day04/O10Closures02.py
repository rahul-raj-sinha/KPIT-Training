
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(name):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" +  sep + ": " + name)
            print(emojized)

        return innerMostFun

    return innerFun

KanGrt = outerFun("Namaskara")
TgrKanGrt = KanGrt("lion")

TgrKanGrt("Prabhakar")

"""
outerFun("Hello")("====>>")("Sourav")

EngGrt = outerFun("Hello")

EngrtSngArw = EngGrt("------->")
EngrtDblArw = EngGrt("=======>>")


EngrtSngArw("Sachin")
EngrtDblArw("Rahul")
"""