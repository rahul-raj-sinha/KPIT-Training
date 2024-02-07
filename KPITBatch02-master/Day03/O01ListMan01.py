
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 9.0, 10.2, 11.5,
      12.7,True, False, 3 + 4j, 5 - 8j]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD

# Create
l1 = list(range(1, 11))
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
# Read
print(f"l1[0] :{l1[0]}")
print(f"l1[6] :{l1[6]}")
# iterate
for i in l1:
    print(i, end=" ")
print()
print("-" * 60)
for i in range(0, len(l1)):
    print(l1[i], end=" ")
print()

#update - modify, add
print("-" * 60)
print(f"l1 :{l1}")

#add new element
l1[4] = 500
l1[7] = 800

print(f"l1 :{l1}")

print("-" * 60)
# Delete
print(f"l1 :{l1}")
del l1[3]
del l1[6]

print(f"l1 :{l1}")

print("-" * 60)
print(f"l1 :{l1}")

# error - index out of range
# l1[15] = 150

print("-" * 60)
print(dir(l1))
