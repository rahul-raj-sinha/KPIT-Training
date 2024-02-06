
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


for i in range(1, 100000):
    res = 0
    j = str(i)
    for k in range(0, len(j)):
        res = fact(int(j[k])) + res

    if i == res:
        print(i)