
for i in range(25, 50):

    for j in range(3):
        if i % 3 == 1:
            n1 = i // 3 + 1
            n2 = i - n1
            i = n2
        else:
            break

if (i % 3 == 0):
    print(i)