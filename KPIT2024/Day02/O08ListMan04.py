"""

sort - this will sort the original list
sorted - will return a copy of the sorted list, original list will remain the same (unsorted)

"""

l1 = [8, 10, 1, 6, 2, 9, 4, 5, 3, 7]
print(f"l1 :{l1}")

# Sort the elements of the list

asc_num = sorted(l1)
print(f"the ascending order of numbers is :{asc_num}")

desc_num = sorted(l1, reverse=True)
print(f"The descending order of numbers is :{desc_num}")

print("-" * 60)

l2 = [8,'apple', 'zebra', 10, 'yellow', 'blue', 1, 'white', 'cat', 6, 'violet', 'dog', 2, 'green', 'pink', 9, 'orange', 'mango', 4, 'egg', 'queen', 5, 3, 7, 1009, 123, 1459, 29, 230, 2560, 2210]

print(f"l2 :{l2}")

res = sorted(l2, key=ascii)
print()
print(f"res :{res}")

print("-" * 60)

cities = ['thiruvananthapuram', 'delhi', 'bangalore', 'vishakapatnam', 'ooty', 'pune', 'hyderabad', 'mysore', 'coimbatore', 'chennai']

# sort the list by the length of the city names

res_asc = sorted(cities, key=len)
print(res_asc)

print()
res_desc = sorted(cities, key=len, reverse=False)
print(res_desc)

print("-" * 60)

l1 = [8, 10, 1, 6, 2, 9, 4, 5, 3, 7]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")