
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)

t2 = (1, 2, 3, 4, 'five', 'six', 7.2, 8.5, 9+0j, 10-2j, True, False)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)

t3 = tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)

t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

# arr = list(range(1, 11)),
# print(arr)
# print(type(arr))

print("-" * 60)

t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

print("-" * 60)
t1 = tuple(range(1, 11))
print(f"t1[0] :{t1[0]}")

# t1[4] = 30

# print(dir(t1))

print("-" * 60)

# count

t1 = (1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1, 2, 3)

print(f"1 :{t1.count(1)}")
print(f"2 :{t1.count(2)}")
print(f"3 :{t1.count(3)}")

print("-" * 60)   
# index
print(t1.index(3))
print(t1.index(3, t1.index(3) + 1))
print(t1.index(3, t1.index(3, t1.index(3) + 1) + 1))
