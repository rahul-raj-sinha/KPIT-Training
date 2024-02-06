
values = list(range(10, 40, 10))
print(values)

# upack
a, b, c = values
print(a, b, c, sep=", ")

values = list(range(10, 101, 10))
print(values)

a, b, *c = values
print(a, b, c, sep=", ")
print()
a, *b, c = values
print(a, b, c, sep=", ")
print()
*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)

lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(lst3)
print(len(lst3))

print("-" * 60)

lst3 = [*lst1, *lst2]
print(lst3)
print(len(lst3))