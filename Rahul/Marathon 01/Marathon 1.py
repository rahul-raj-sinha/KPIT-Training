# Question 1
def ODD(n):
    matrix = [[0 for x in range(n)] for y in range(n)]

    # initialize position of 1
    r = n // 2
    c = n - 1

    # Filling the matrix by placing values
    num = 1
    while num <= (n * n):
        if r == -1 and c == n:  # 3rd condition
            c = n - 2
            r = 0
        else:
            if c == n:
                c = 0
            if r < 0:
                r = n - 1

        if matrix[int(r)][int(c)]:  # 2nd condition
            c = c - 2
            r = r + 1
            continue
        else:
            matrix[int(r)][int(c)] = num
            num = num + 1

        c = c + 1
        r = r - 1  # 1st condition

    # Printing matrix
    print("N =", n)
    print("Sum of each row, column and diagonal is: ",
          n * (n * n + 1) // 2, "\n")

    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (matrix[i][j]),
                  end='')

            # To display output in matrix form
            if j == n - 1:
                print()


n=int(input("Enter Odd Number: "))
ODD(n)
