
# print numbers between 150 and 50
n = 0
for i in range(150, 49, -1):
    # print(i, end=" ")

    cntr = 0
    for j in range(2, i):

        if i % j == 0:
            break
    else:
        print(i, end= " ")
        n += 1


print()
print(f"There are {n} prime numbers between 150 and 50")

print("-" * 60)

cntr = 0
for i in range(1, 5):
    for j in range(0,i):
        cntr += 1
        print(cntr, end=" ")
    print()

print("-" * 60)

