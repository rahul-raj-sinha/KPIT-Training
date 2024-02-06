
# map

l1 = list(range(1, 11))
print(f"l1 :{l1}")

squares = list(map(lambda x: x ** 2, l1))
print(f"squares :{squares}")

print("-" * 60)

# Sort the months

months = ['dec', 'aug', 'apr', 'nov', 'feb', 'oct', 'jan', 'mar', 'may', 'jul', 'sep', 'jun']
from calendar import month_abbr

# print(list(month_abbr))

print("Months :{months}")
res = sorted(months, key = list(map(lambda x: x.lower(), list(month_abbr))).index)
print(f"res :{res}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"

res = list(map(lambda x: x.upper(), sentence.split()))
print(f"res :{res}")

print("-" * 60)
# filter

l1 = list(range(1, 25))

res = list(filter(lambda x : x % 2 == 1, l1))
print(f"res :{res}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"

res = list(filter(lambda x: x != 'the', sentence.split()))
print(f"res :{res}")

# convert the list into a string
st = " ".join(res)
print(st)

print("-" * 60)
# reduce

from functools import reduce

l1 = [9, 7, 4, 8, 10, 2, 1, 5, 3, 6]
print(f"l1 :{l1}")

lrgst = reduce(lambda x, y: x if x > y else y, l1)
print(f"Largest :{lrgst}")

res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")
