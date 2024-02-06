import math

l1 = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
# print the sum of all numbers

x = 0
for i in l1:
    x += i

print(f"The sum of all number in the list :{x}")

print("=" * 60)

l1 = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
# print all even numbers and odd numbers seperately
odd = []
even = []

for i in l1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f'Even Numbers :{even}')
print(f"Odd Numbers :{odd}")

print("=" * 60)

l2 = [10, 1, 9, 3, 5, 12, 8, 6, 2]
    # print the largest number in the list

print(f"l2 :{l2}")

temp = 0
for i in range(0, len(l2)-1):
    if l2[i] > temp:
        temp = l2[i]

print(f"The largest number is :{temp}")

# print the smallest number in the list
temp = max(l2)
for i in range(0, len(l2)-1):
    if l2[i] < temp:
        temp = l2[i]

print(f"The smallest number is :{temp}")

# print the second largest number in the list

l2 = [10, 1, 9, 3, 5, 12, 8, 6, 2]
temp = 0
temp2 = 0
for i in range(0, len(l2)-1):
    if l2[i] > temp:
        temp = l2[i]

temp2 = temp
for i in range(0, len(l2)-1):
    if (l2[1] != temp and l2[i] < temp2):
        temp2 = l2[i]

print(temp2)


# print the second smallest number in the list


l2 = [10, 1, 9, 3, 5, 12, 8, 6, 2]
temp = max(l2)
temp2 = max(l2)

for i in range(0, len(l2)):
   if l2[i] < temp:
     temp = l2[i]

for i in range(0, len(l2)):
   if l2[i] != temp and l2[i] < temp2:
     temp2 = l2[i]

print(f"The second smallest number is :{temp2}")


