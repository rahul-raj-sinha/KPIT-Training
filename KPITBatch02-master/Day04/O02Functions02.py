
# immutable dictionary

from collections import namedtuple


# nmdTpl = namedtuple("Arithmetic", "sum diff prod quot"])
def arithmeticCalc(x, y):
    nmdTpl = namedtuple("Arithmetic", ["sum", "diff", "prod", "quot"])
    s = x + y
    d = x - y
    p = x * y
    q = x / y

    resTpl = nmdTpl(sum = s, diff = d, prod = p, quot = q)

    return resTpl



res =  arithmeticCalc(20, 8)
print(res)

print(f"Sum        :{res.sum}")
print(f"Difference :{res.diff}")
print(f"Product    :{res.sum}")
print(f"Quotent    :{res.sum}")
