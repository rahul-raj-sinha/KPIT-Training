
# largest

temp = 0
l2 = [10, 1, 9, 3, 5, 12, 8, 6, 2]

for i in range(0, len(l2) - 1):
    if l2[i] > temp:
        temp = l2[i]

print(f"The largest number is :{temp}")

print("=" * 60)

import math
temp = math.inf

for i in range(0, len(l2)- 1):
    if l2[i] < temp:
        temp = l2[i]

print(f"The smallest number is :{temp}")
