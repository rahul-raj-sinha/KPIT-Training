
def add(x, y):
    return x + y

a = add
print(a(100, 200))

print("-" * 60)

b = lambda i, j: i + j

print(b(10, 20))