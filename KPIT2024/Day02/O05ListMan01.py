
l1 = list()
print(l1)
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3,4, 'five', 'six', 'seven', 'eight', 9.2, 10.7, 11.25, 2 + 0j, 2 + 1j ]
print(f"l2 :{l2}")
print(type(l2))
print(f"l2[0] :{l2[0]}")

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
l1 = list(range(10, 101, 10))
print(f"l1 :{l1}")

#insert
l1[2] = 25
print(f"l1 :{l1}")

# update
# l1[15] = 150
l1[5] =  500
print(f"l1 :{l1}")

# delete
del l1[3]
print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))

