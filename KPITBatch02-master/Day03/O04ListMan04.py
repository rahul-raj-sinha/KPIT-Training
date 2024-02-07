
l1 = [10, 4, 9, 1, 6, 8, 2, 5, 7, 3]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending Order :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending Order :{res_desc}")

print("-" * 60)

l1 = (10, 'zebra', 4,'apple', 9, 'yellow', 'blue', 1, 'violet', 'green', 6, 'pink', 'red', 8, 'orange', 'cat', 2, 'dog', 'maroon', 5, 'white', 7, 3, 192, 1234, 29, 270, 2345)

print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(f"res :{res}")

idx = 0
for i in range(0, len(res)):
    if type(res[i]) == int:
        idx = i
        break

print("-" * 60)
res = res[1:13] + sorted(res[13:])
print(f"res :{res}")

print("-" * 60)
cities = ['vishakapatnam', 'mumbai', 'pune', 'thiruvananthapuram', 'chennai', 'bangalore', 'delhi', 'ooty', 'kolkota']

print(f"cities :{cities}")

res = sorted(cities, key=len)
print("-" * 60)
print(f"res :{res}")

print("reverse".center(60, "-"))
l1 = [10, 4, 9, 1, 6, 8, 2, 5, 7, 3]
print(f"l1 :{l1}")

l1.reverse()
print(f"l1 :{l1}")

cities.reverse()
print(cities)