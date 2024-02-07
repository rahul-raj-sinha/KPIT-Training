
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)
        return innerMostFun

    return innerFun
# ------------------------------
engTgr = outerFun("Welcome")
engTgrGrt = engTgr("lion")
engTgrGrt("Sherof")

"""
engGrt = outerFun("Welcome")
tmlGrt = outerFun("Vanakam")

engGrtSngArw = engGrt("------>")
engGrtDblArw = engGrt("======>>")
tmlGrtSngArw = tmlGrt("------>")
tmlGrtDblArw = tmlGrt("======>>")

engGrtSngArw("Rahul")
engGrtDblArw("Sachin")
tmlGrtSngArw("Ashwin")
tmlGrtDblArw("Srikanth")
"""