# # A basic code for matrix input from user
#
# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))
#
# # Initialize matrix
# matrix = []
# print("Enter the entries rowwise:")
#
# # For user input
# for i in range(R):		 # A for loop for row entries
# 	a =[]
# 	for j in range(C):	 # A for loop for column entries
# 		a.append(int(input()))
# 	matrix.append(a)
#
# # For printing the matrix
# for i in range(R):
# 	for j in range(C):
# 		print(matrix[i][j], end = " ")
# 	print()
#
#
#
#
# # one-liner logic to take input for rows and columns
# mat = [[int(input()) for x in range (C)] for y in range(R)]
#



# Magic Matrix for ODD
# # Python program to generate
# # odd sized magic squares
# # A function to generate odd
# # sized magic squares
#
#
# def generateSquare(n):
#
# 	# 2-D array with all
# 	# slots set to 0
# 	magicSquare = [[0 for x in range(n)]
# 				for y in range(n)]
#
# 	# initialize position of 1
# 	i = n // 2
# 	j = n - 1
#
# 	# Fill the magic square
# 	# by placing values
# 	num = 1
# 	while num <= (n * n):
# 		if i == -1 and j == n: # 3rd condition
# 			j = n - 2
# 			i = 0
# 		else:
#
# 			# next number goes out of
# 			# right side of square
# 			if j == n:
# 				j = 0
#
# 			# next number goes
# 			# out of upper side
# 			if i < 0:
# 				i = n - 1
#
# 		if magicSquare[int(i)][int(j)]: # 2nd condition
# 			j = j - 2
# 			i = i + 1
# 			continue
# 		else:
# 			magicSquare[int(i)][int(j)] = num
# 			num = num + 1
#
# 		j = j + 1
# 		i = i - 1 # 1st condition
#
# 	# Printing magic square
# 	print("Magic Square for n =", n)
# 	print("Sum of each row or column",
# 		n * (n * n + 1) // 2, "\n")
#
# 	for i in range(0, n):
# 		for j in range(0, n):
# 			print('%2d ' % (magicSquare[i][j]),
# 				end='')
#
# 			# To display output
# 			# in matrix form
# 			if j == n - 1:
# 				print()
#
# # Driver Code
#
#
# # Works only when n is odd
# n = 7
# generateSquare(n)
#

# Magic Mattrix for Even
# Python program to print magic square of double order

# def DoublyEven(n):
#     # 2-D matrix with all entries as 0
#     arr = [[(n * y) + x + 1 for x in range(n)] for y in range(n)]
#
#     # Change value of array elements at fix location
#     # as per the rule (n*n+1)-arr[i][[j]
#
#     # Corners of order (n/4)*(n/4)
#     # Top left corner
#     for i in range(0, n // 4):
#         for j in range(0, n // 4):
#             arr[i][j] = (n * n + 1) - arr[i][j];
#
#         # Top right corner
#     for i in range(0, n // 4):
#         for j in range(3 * (n // 4), n):
#             arr[i][j] = (n * n + 1) - arr[i][j];
#
#         # Bottom Left corner
#     for i in range(3 * (n // 4), n):
#         for j in range(0, n // 4):
#             arr[i][j] = (n * n + 1) - arr[i][j];
#
#         # Bottom Right corner
#     for i in range(3 * (n // 4), n):
#         for j in range(3 * (n // 4), n):
#             arr[i][j] = (n * n + 1) - arr[i][j];
#
#         # Centre of matrix,order (n/2)*(n/2)
#     for i in range(n // 4, 3 * (n // 4)):
#         for j in range(n // 4, 3 * (n // 4)):
#             arr[i][j] = (n * n + 1) - arr[i][j];
#
#         # Printing the square
#     for i in range(n):
#         for j in range(n):
#             print('%2d ' % (arr[i][j]), end=" ")
#         print()
#
#     # Driver Program
#
#
# n = 8
# DoublyEven(n)






# Magic Matrix
#Function
# def generateSquare(n):
#     # 2-D array with all
#     # slots set to 0
#     magicSquare = [[0 for x in range(n)]
#                       for y in range(n)]
#     # initialize position of 1
#     i = n / 2
#     j = n - 1
#     # Fill the square by placing values
#     num = 1
#     while num <= (n * n):
#         if i == -1 and j == n: # 3rd condition
#             j = n - 2
#             i = 0
#         else:
#             # next number goes out of
#             # right side of square
#             if j == n:
#                 j = 0
#             # next number goes
#             # out of upper side
#             if i < 0:
#                 i = n - 1
#         if magicSquare[int(i)][int(j)]: # 2nd condition
#             j = j - 2
#             i = i + 1
#             continue
#         else:
#             magicSquare[int(i)][int(j)] = num
#             num = num + 1
#         j = j + 1
#         i = i - 1 # 1st condition
#     # Printing the square
#     print ("Magic Square for n =", n)
#     print ("Sum of each row or column",n * (n * n + 1) / 2, "\n")
#     for i in range(0, n):
#         for j in range(0, n):
#             print('%2d ' % (magicSquare[i][j]),end = '')
#             # To display output
#             # in matrix form
#             if j == n - 1:
#                 print()
# # Driver Code
# # Works only when n is odd
# n=int(input("Number of rows of the Magic Square:"))
# generateSquare(n)




# # Program to add two matrices using nested loop
# X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# # iterate through rows
# for row in range(len(X)):
#
# 	# iterate through columns
# 	for column in range(len(X[0])):
# 		result[row][column] = X[row][column] + Y[row][column]
#
# for r in result:
# 	print(r)
#



# Adding and subtracting values to a matrix with list comprehension
# Add_result = [[X[row][column] + Y[row][column]
# 			   for column in range(len(X[0]))]
# 			  for row in range(len(X))]
# Sub_result = [[X[row][column] - Y[row][column]
# 			   for column in range(len(X[0]))]
# 			  for row in range(len(X))]
#
# print("Matrix Addition")
# for r in Add_result:
# 	print(r)
#
# print("\nMatrix Subtraction")
# for r in Sub_result:
# 	print(r)
#
#
#
#
#
#Python program to multiply and divide two matrices
#
# rmatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# for row in range(len(X)):
# 	for column in range(len(X[0])):
# 		rmatrix[row][column] = X[row][column] * Y[row][column]
#
# print("Matrix Multiplication", )
# for r in rmatrix:
# 	print(r)
#
# for i in range(len(X)):
# 	for j in range(len(X[0])):
# 		rmatrix[row][column] = X[row][column] // Y[row][column]
#
# print("\nMatrix Division", )
# for r in rmatrix:
# 	print(r)
#





# Transpose
# X = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# # iterate through rows
# for row in range(len(X)):
# 	# iterate through columns
# 	for column in range(len(X[0])):
# 		result[column][row] = X[row][column]
#
# for r in result:
# 	print(r)
#
# # # Python Program to Transpose a Matrix using the list comprehension
#
# # rez = [[X[column][row] for column in range(len(X))]
# #    for row in range(len(X[0]))]
#
# # for row in rez:
# #     print(row)






#
# Magice Matrix for any number
# def generateOddSquare(n):
#     magicSquare = [[0]*n for i in range(n)]
#     i = n // 2
#     j = n - 1
#     num = 1
#     while num <= (n * n):
#         if i == -1 and j == n:
#             j = n - 2
#             i = 0
#         else:
#             if j == n:
#                 j = 0
#             if i < 0:
#                 i = n - 1
#
#         if magicSquare[int(i)][int(j)]:
#             j = j - 2
#             i = i + 1
#             continue
#         else:
#             magicSquare[int(i)][int(j)] = num
#             num = num + 1
#
#         j = j + 1
#         i = i - 1
#
#     for i in range(0, n):
#         for j in range(0, n):
#             print(magicSquare[i][j], end=' ')
#         print()
#
#
# def generateDoublyEvenSquare(n):
#     arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)]
#
#     for i in range(0, n//4):
#         for j in range(0, n//4):
#             arr[i][j] = (n*n + 1) - arr[i][j]
#
#     for i in range(0, n//4):
#         for j in range(3 * (n//4), n):
#             arr[i][j] = (n*n + 1) - arr[i][j]
#
#     for i in range(3 * (n//4), n):
#         for j in range(0, n//4):
#             arr[i][j] = (n*n + 1) - arr[i][j]
#
#     for i in range(3 * (n//4), n):
#         for j in range(3 * (n//4), n):
#             arr[i][j] = (n*n + 1) - arr[i][j]
#
#     for i in range(n//4, 3 * (n//4)):
#         for j in range(n//4, 3 * (n//4)):
#             arr[i][j] = (n*n + 1) - arr[i][j]
#
#     for i in range(n):
#         for j in range(n):
#             print('%2d ' % (arr[i][j]), end=" ")
#         print()
#
#
# def generateSinglyEvenSquare(n):
#     magicsqr = [[0]*n for i in range(n)]
#     halfN = n // 2
#     k = (n-2)//4
#     temp = 0
#     swapCol = []
#     index = 0
#     miniMagic = [[0]*halfN for i in range(halfN)]
#     miniMagic = odd(miniMagic)
#
#     for i in range(halfN):
#         for j in range(halfN):
#             magicsqr[i][j] = miniMagic[i][j]
#             magicsqr[i+halfN][j+halfN] = miniMagic[i][j] + halfN*halfN
#             magicsqr[i][j+halfN] = miniMagic[i][j] + 2*halfN*halfN
#             magicsqr[i+halfN][j] = miniMagic[i][j] + 3*halfN*halfN
#
#     for i in range(1, k+1):
#         swapCol.append(i)
#
#     for i in range(n-k+2, n+1):
#         swapCol.append(i)
#
#     for i in range(1, halfN+1):
#         for j in range(1, len(swapCol)+1):
#             temp = magicsqr[i-1][swapCol[j-1]-1]
#             magicsqr[i-1][swapCol[j-1]-1] = magicsqr[i+halfN-1][swapCol[j-1]-1]
#             magicsqr[i+halfN-1][swapCol[j-1]-1] = temp
#
#     temp = magicsqr[k][0]
#     magicsqr[k][0] = magicsqr[k+halfN][0]
#     magicsqr[k+halfN][0] = temp
#
#     temp = magicsqr[k+halfN][k]
#     magicsqr[k+halfN][k] = magicsqr[k][k]
#     magicsqr[k][k] = temp
#
#     for i in range(len(magicsqr)):
#         for j in range(len(magicsqr[0])):
#             print(magicsqr[i][j], end=' ')
#         print()
#
#
# def odd(magic):
#     n = len(magic)
#     row = n - 1
#     col = n // 2
#     magic[row][col] = 1
#     for i in range(2, n * n + 1):
#         if magic[(row+1) % n][(col+1) % n] == 0:
#             row = (row + 1) % n
#             col = (col + 1) % n
#         else:
#             row = (row - 1 + n) % n
#         magic[row][col] = i
#     return magic
#
#
# n = int(input("Value Of N? "))
# if n == 2:
#     sq = [[1, 1], [1, 1]]
#     for i in range(len(sq)):
#         for j in range(len(sq)):
#             print(sq[i][j], end=' ')
#         print()
# elif n % 2 == 1:
#     generateOddSquare(n)
# elif n % 4 == 0:
#     generateDoublyEvenSquare(n)
# else:
#     generateSinglyEvenSquare(n)





# Magic Matrix (1)
#
# def matrix(n):
#     m = [[0 for x in range(n)]for y in range(n)]
#     i = n // 2
#     j = n - 1
#     num = 1
#     while num <= (n * n):
#         if i == -1 and j == n:
#             j = n - 2
#             i = 0
#         else:
#             if j == n:
#                 j = 0
#             if i < 0:
#                 i = n - 1
#         if m[int(i)][int(j)]:
#             j = j - 2
#             i = i + 1
#             continue
#         else:
#             m[int(i)][int(j)] = num
#             num = num + 1
#         j = j + 1
#         i = i - 1
#     print ("Sum of eggs in each row or column and diagonal : ",int(n*(n*n+1)/2),"\n")
#     for i in range(0, n):
#         for j in range(0, n):
#             print('%2d ' % (m[i][j]),end = '')
#             if j == n - 1:
#                 print()
#
# n=int(input("Number of rows of the matrix : "))
# matrix(n)






# if "n" is  an odd integer

# Starting from the first position after verifying it's Odd

# r = n // 2
# c = n - 1
# i = 1
# limit = n ** 2
#
# # here limit is the range of eggs that we can arrange in the basket
#
# while i <= limit:
#     if r == -1 and c == n:  # Condition if both the rows and columns are out of range
#         r = 0
#         c = n - 2
#     else:
#
#         if r < 0:  # Condition if rows are out of range
#             r = n - 1
#
#         if c == n:  # Condition if column out of range
#             c = 0
#
#     if matrix[r][c]:  # Starting to arrange
#         c = c - 2
#         r = r + 1
#         continue
#
#     else:  # Condition if the before condition becomes False
#         matrix[r][c] = i
#
#         i += 1  # Increment of the " i " value
#
#     c += 1  # Increment of column
#
#     r -= 1  # Decrement of rows to skip to another value
#
#     '''Printing the number of Rows '''
# print("basket for n =", n)
#
# # Print the sum of each row and column of n order matrix
#
# print("Sum of each row or column", n * (n * n + 1) / 2, "\n")
#
# '''Printing the Basket '''
#
# print("Basket with arrangement of EGGS is : ")
#
# # Used Nested list
# for r in range(0, n):
#     for c in range(0, n):
#         print("%2d" % (matrix[r][c]), end="    ")
#         # To display output
#         # in matrix form
#         if c == n - 1:
#             print()


# # Condition to change the zero elements is (n*n+1)-matrix[r][c]
# # Starting with Top left corner
# for r in range(n // 4):  # setting a range to rows
#
#     for c in range(n // 4):  # setting a range to column
#
#         matrix[r][c] = (n * n - 1) - matrix[r][c];
#
#         # Moving to Top right corner
#
# for r in range(n // 4):
#
#     for c in range(3 * (n // 4), n):
#         matrix[r][c] = (n * n + 1) - matrix[r][c];
#
#     # Moving Bottom Left corner
#
# for r in range(3 * (n // 4), n):
#
#     for c in range(0, n // 4):
#         matrix[r][c] = (n * n + 1) - matrix[r][c];
#
#     # Moving to Bottom Right corner
#
# for r in range(3 * (n // 4), n):
#
#     for c in range(3 * (n // 4), n):
#         matrix[r][c] = (n * n - 1) - matrix[r][c];
#
#     # Center of matrix,order(n/2)*(n/2)
#
# for r in range(n // 4, 3 * (n // 4)):
#
#     for c in range(n // 4, 3 * (n // 4)):
#         matrix[r][c] = (n * n - 1) - matrix[r][c];
#
# print("basket for n =", n)
#
# print("Sum of each row or column", n * (n * n + 1) / 2, "\n")