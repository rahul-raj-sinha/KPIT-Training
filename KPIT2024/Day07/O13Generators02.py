
def fun():
    n = 1
    print("apples from ooty......")
    yield n
    n += 9
    print("Oranges from nagpur.....")
    yield n
    n += 10
    print("grapes from hubli.......")
    yield n

res = fun()
print(f"res :{res}")
print(type(res))

print("-" * 60)
print(res.__next__())

print("-" * 60)
print(res.__next__())

print("-" * 60)
print(res.__next__())

# print("-" * 60)
# print(res.__next__())

print("-" * 60)
def fun():
    for i in range(1, 11):
        yield i

fn = fun()
print(fn.__next__())
print(next(fn))
print(next(fn))

print("-" * 60)
for x in fun():
    print(x, end=" ")
print()

