# class StartStopwitharguement:
#     def __init__(self,arg1,arg2,arg3):
#         self.arg1=arg1
#         self.arg2=arg2
#         self.arg3=arg3
#
#     def __call__(self, fnc):
#         def innerFun(x,y):
#             print(f"class Deco starts")
#             print(f"(self.arg1),(self.arg2),(self.arg3)")
#             fnc(x,y)
#             print("class Deco ends")
#
#         return innerFun
