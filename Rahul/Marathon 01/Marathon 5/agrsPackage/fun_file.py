# def dec_with_arg(*args):
#     def deco(fnc):
#         def innerFun(x,y):
#             print(f"Decorator with arg start")
#             print(f"(args")
#             fnc(x,y)
#             print(f"Decorator with arg end")
#         return innerFun
#     return deco

# def test(x, y, z):
#     def inner(fnc):
#         def innermost(a, b):
#             fnc(a, b)
#
#         return innermost
#
#     return inner
