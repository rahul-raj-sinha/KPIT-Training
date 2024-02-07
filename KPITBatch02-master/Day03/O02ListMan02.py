
print("{txt:-^60}".format(txt="append"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")
print(type(l1))

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(l1[8][1:4])

print("-" * 60)
# extend
l2 = list(range(5, 11))
print(f"l2 :{l2}")
print(type(l2))

l2.extend([11, 12, 13, 14, 15])
print(F"l2 :{l2}")

l2.extend(list(range(16, 21)))
print(f"l2 :{l2}")

print("insert".center(60, "-"))
l1 = [3, 4, 5]
print(f"l1 :{l1}")
print(type(l1))

l1.insert(0, 2)
l1.insert(0, 1)
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

print("pop".center(60, "-"))
l1 = list(range(1, 21))
print(f"l1: {l1}")
print(type(l1))

res = l1.pop(7)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop(14)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2,2, 1, 2, 3, 1, 1, 1,1,1, 1, 2, 3, 1, 2,1, 1,1, 1,2,2,2,2,2,2,2, 1,1, 1,1 , 1 ,1,1 ,1, 1, 1,]

l1.remove(3)
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

# error
# l1.remove(5)
# print(f"l1 :{l1}")

while(1 in l1):
    l1.remove(1)
print(l1)

print("-" * 60)


while(l1.count(2)):
    l1.pop(l1.index(2))
print(f"l1 :{l1}")