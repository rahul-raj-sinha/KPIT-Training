
from functools import reduce

lst = [9, 3, 5, 7, 2, 4, 10, 6]
print(f"lst :{lst}")

res = reduce(lambda x, y: x if x > y else y, lst)
print(f"res :{res}")

res = reduce(lambda x,y: x + y, lst)
print(f"res :{res}")