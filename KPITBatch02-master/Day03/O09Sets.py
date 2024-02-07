
s1 = set()
print(f"s1 :{s1}")
print(type(s1))
print("-" * 60)

s2 = {1, 2, 3, 4, 5}
print(f"s2 :{s2}")
print(type(s2))
print("-" * 60)

# print(dir(s1))
# print("-" * 60)
s1 = {1, 2, 3}
print(f"s1 :{s1}")

# add
s1.add(4)
s1.add(5)
s1.add(2)
s1.add(1)
s1.add(6)
s1.add(3)

print(f"s1 :{s1}")

print("-" * 60)
# update
s1.update([2, 3, 4])
s1.update([5, 6, 7])
s1.update([4, 5, 6])
s1.update([7, 8, 9])
s1.update([10, 1, 2])
print(f"s1 :{s1}")

print("-" * 60)
# pop
res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1: {s1}")

print("-" * 60)
# remove
s1.remove(8)
s1.remove(6)

print(f"s1 :{s1}")
# s1.remove(1)

print("-" * 60)
# discard

s1.discard(4)
s1.discard(1)

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 60)
print(f"A union B : {A | B}")
print(f"A union B : {A.union(B)}")

print("-" * 60)
print(f"A intersection B :{A & B}")
print(f"A intersection B :{A.intersection(B)}")

print("-" * 60)
print(f"A difference B :{A - B}")
print(f"A differnece B :{A.difference(B)}")

print("-" * 60)
print(f"A symmetric difference B :{A ^ B}")
print(f"A symmetric difference B :{A.symmetric_difference(B)}")

print("-" * 60)
# frozenset
A = frozenset({1, 2, 3, 4, 5})
print(f"A :{A}")
print(type(A))
