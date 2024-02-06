#
# def outerFun():         # HOF Higher Order Function
#     gname = "Sachin"
#     def InnerFun():
#
#         print('Hello World')
#         print(f"Greetings Mr.{gname}")
#
#     return InnerFun
#
# Inref = outerFun()
# Inref()
#
# print("-" * 60)
#
# outerFun()()            # calls the innerFun
#
#
#

#
# def outerFun(greet):
#
#     # simple Curry
#     def innerFun(gname):
#
#         print(greet, gname)
#
#     return innerFun
#
# outerFun("Hello")("Sachin")
#
# EngGrt = outerFun("Hello")
# HndGrt = outerFun("Namaskar")
# TmlGrt = outerFun("Vanakam")
#
# EngGrt("Rahul")
# HndGrt("Shami")
# TmlGrt("Natrajan")


# def outerFun(greet):
#     def innerFun(sep):
#         def innerMostFun(gname):
#             from emojis import emojis
#             emojized = emojis.encode(greet + " :" + sep + ": " + gname)
#             print(emojized)
#
#         return innerMostFun
#
#     return innerFun
#
#
# # ------------------------------
# engTgr = outerFun("Welcome")
# engTgrGrt = engTgr("lion")
# engTgrGrt("Sherof")
#
# """
# engGrt = outerFun("Welcome")
# tmlGrt = outerFun("Vanakam")
#
# engGrtSngArw = engGrt("------>")
# engGrtDblArw = engGrt("======>>")
# tmlGrtSngArw = tmlGrt("------>")
# tmlGrtDblArw = tmlGrt("======>>")
#
# engGrtSngArw("Rahul")
# engGrtDblArw("Sachin")
# tmlGrtSngArw("Ashwin")
# tmlGrtDblArw("Srikanth")
# """
