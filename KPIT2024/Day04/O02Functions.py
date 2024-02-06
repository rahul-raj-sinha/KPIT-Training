
from collections import namedtuple
def arithCalc(x, y):
    s = x + y
    d = x - y
    p = x * y
    q  = x / y

    nmdTpl = namedtuple("Arith", "sum diff prod quot")
    arthObj = nmdTpl(sum=s, diff=d, prod=p, quot=q)
    return arthObj

res = arithCalc(20, 6)
print(res)

print(f"Sum of the numbers          :{res.sum}")
print(f"Difference of the numbers   :{res.diff}")
print(f"Product of the numbers      :{res.prod}")
print(f"Quotient of the numbers     :{res.quot}")


