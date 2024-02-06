
print("Append".center(60, "-"))
l1 = list(range(1,6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)

print(f"l1 :{l1}")

l1.append([10, 11, 12, 13, 14, 15])
print(f"l1 :{l1}")

print(f"l1[9][2:5] :{l1[9][2:5]}")

print("Extend".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.extend([6, 7, 8])
print(f"l1 :{l1}")

print("Insert".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"1l :{l1}")

res = l1.pop(7)
print(f"res :{res}")
print(F"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 2, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 2, 1, 2, 2, 1, 1, 2, 3, 1, 2,1,1, 1,1, 2,2,2 ,2,2,2,2,2,2,1, 2, 1,1,1,1]

print(f"l1 :{l1}")

l1.remove(3)
l1.remove(3)
l1.remove(3)

print("-" * 60)
print(f"l1 :{l1}")

while(l1.count(1)):
    l1.remove(1)

print(f"l1 :{l1}")


print("clear".center(60, "-"))

l1 = list(range(1, 11))

print(f"l1 :{l1}")

l1.clear()

print(f"l:{l1}")

print("count".center(60, "-"))

l1 = [1, 2,3, 4, 1, 2, 3, 4,1, 1,1,1 , 1, 2, 2]

print("1 :", l1.count(1))
print("2 :", l1.count(2))
print("3 :", l1.count(3))
print("5 :", l1.count(5))