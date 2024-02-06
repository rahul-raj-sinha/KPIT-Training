
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 60)

s2 = {1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 9.5, 10.1, 11+1j, 12-15j, True, False}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 60)

s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 60)
# print(dir(s1))

s1 = {1, 2}
# add - add one value into the set

s1.add(3)
s1.add(1)
s1.add(4)
s1.add(2)
s1.add(5)

print(f"s1 :{s1}")

print("-" * 60)
# update - can add more than one value

s1.update([1, 2, 3])
s1.update([2, 3, 4])
s1.update([4, 5, 6])
s1.update([3, 4, 5])
s1.update([7, 8, 9])
s1.update([6, 7, 8])

print(f"s1 :{s1}")

print("-" * 60)
# pop, discard, remove

print(f"s1 :{s1}")

res = s1.pop()
print(f"res :{res}")
print(f"s1 :{s1}")

res = s1.pop()
print(f"res :{res}")

print("-" * 60)

s1.remove(5)
s1.remove(8)

print(f"s1 :{s1}")

# s1.remove(1)
print("-" * 60)
# discard

s1.discard(4)
print(f"s1 :{s1}")

s1.discard(1)

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(F"A :{A}")
print(f"B :{B}")

print("-" * 60)

print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print("-" * 60)
print(f"A intersection of B :{A & B}")
print(f"B intersection of A :{B.intersection(A)}")

print("-" * 60)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 60)
print(f"A symmetric difference B :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

print("-" * 60)
# frozen set - immutable

s2 = frozenset([1, 2, 3, 4, 5])
print(f"s2 :{s2}")
print(type(s2))
