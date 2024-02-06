

# copy function
print("-" * 60)
l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")

# copy from l3 to l4

l4 = l3.copy()              # deep copy - only data gets copied

print(f"l4 before :{l4}")

l4.append(11)
l4.append(12)
l4.append(13)

print(f"l3 after :{l3}")
print(f"l4 after :{l4}")

print("-" * 60)

l5 = [11, 12, 13, 14, [1, 2, 3, 4, 5], 15]
print(f"l5 before :{l5}")

# copy from l5 to l6

l6 = l5.copy()

print(f"l6 before :{l6}")

l6[4].extend([6, 7, 8, 9])

print(f"l5 after :{l5}")
print(f"l6 after :{l6}")

print("-" * 60)

from copy import deepcopy
l7 = [10, 20, 30, [2, 4, 6, 8, 10], 40, 50]
print(f"l7 before :{l7}")

l8 = deepcopy(l7)           # deep copy

print(f"l8 before :{l8}")
l8[3].extend([12, 14, 16])

print(f"l7 after :{l7}")
print(f"l8 after :{l8}")

