
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")

print("-" * 60)
# print(dir(l))

iterObj = l.__iter__()
# print(dir(iterObj))

item1 = iterObj.__next__()
print(f"item1 :{item1}")

item2 = iterObj.__next__()
print(f"item2 :{item2}")

item3 = iterObj.__next__()
print(f"item3 :{item3}")

item4 = iterObj.__next__()
print(f"item4 :{item4}")

item5 = iterObj.__next__()
print(f"item5 :{item5}")

# item6 = iterObj.__next__()
# print(f"item6 :{item6}")
print("-" * 60)

for i in l:
    print(i, end=" ")
print()


