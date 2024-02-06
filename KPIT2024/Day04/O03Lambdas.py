
def add(x, y):
    return x + y

res = add(30, 50)
print(f"res :{res}")

a = add
res = a(100, 200)
print(f"res :{res}")

print("-" * 60)
# lambda var1, var2, var3...: expression

b = lambda x, y: x + y
res = b(40, 90)
print(f"res :{res}")
