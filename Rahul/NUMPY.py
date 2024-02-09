# import numpy as np
# arr1 = np.array([2, 3, 4])
# print(arr1)
# print(arr1.ndim)
# print(arr1.dtype)
# print("-" * 60)
# arr2 = np.array([-2, -1, 0, 1, 2])
# print(arr2)
# print(arr2.ndim)
# print(arr2.dtype)
# print("-" * 60)
# arr3 = np.array([0.1, 0.2, 0.3])
# print(arr3)
# print(arr3.ndim)
# print(np.dtype)
# print("-" * 60)
# arr4 = np.array([1, 2, 3, 4, 5], dtype='int32')
# print(arr4)
# print(arr4.dtype)
# print("-" * 60)
# arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(f"dimension: {arr1.ndim}")
# print(f"size: {arr1.size}")
# print(f"shape: {arr1.shape}")
# print(f"itemsize: {arr1.itemsize}")
 









# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(f"arr: {arr}")
# print(type(arr))
# print("-" * 60)
# arr1 = np.array(('a', 'b', 'c', 'd'))
# print(f"arr1: {arr1}")
# print(type(arr1))
# print("-" * 60)
# # dimension
# arr2 = np.array(20)
# print(f"arr2: {arr2}")
# print(type(arr2))
# print()
# print("-" * 60)
# # one dimension
# arr3 = np.array([1, 2, 3, 4, 5])
# print(f"arr3: {arr3}")
# print(arr3)
# print("-" * 60)
# # two dimension
# arr4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
# print(arr4)
# print(type(arr4))
# print("-" * 60)
# # three dimension
# arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(f"arr5: {arr5}")
# print(type(arr5))
# print(f"arr2: {arr2.ndim}")
# print("-" * 60)
# print(f"arr3: {arr3.ndim}")
# print("-" * 60)
# print(f"arr4: {arr4.ndim}")
# print("-" * 60)
# print(f"arr5: {arr5.ndim}")
# print("-"*60)
# arr6 = np.array([1,2,3,4,5], ndmin=5)
# print(f"arr6: {arr6}")
# print(f"arr6: {arr6.ndim}")
# print("-"*60)
# arr7 = np.zeros((2,3))
# print(f"arr7: {arr7}")
# print("-"*60)
# arr8 = np.zeros((2,3,4))
# print(f"arr8: {arr8}")
# print("-"*60)
# arr9 = np.identity(3)
# print(f"arr9: {arr9}")

















# # Matrix Operation using numpy
# import numpy as np

# # Get user input for matrix dimensions
# rows_A = int(input("Enter the number of rows for matrix A: "))
# cols_A = int(input("Enter the number of columns for matrix A: "))
# rows_B = int(input("Enter the number of rows for matrix B: "))
# cols_B = int(input("Enter the number of columns for matrix B: "))

# # Initialize empty matrices
# A = np.empty((rows_A, cols_A))
# B = np.empty((rows_B, cols_B))

# # Get user input for matrix elements
# print("Enter elements for matrix A:")
# for i in range(rows_A):
#     for j in range(cols_A):
#         A[i, j] = float(input(f"Enter element at position ({i}, {j}) for matrix A: "))

# print("Enter elements for matrix B:")
# for i in range(rows_B):
#     for j in range(cols_B):
#         B[i, j] = float(input(f"Enter element at position ({i}, {j}) for matrix B: "))

# # Perform matrix operations
# C = np.dot(A, B)  # Matrix multiplication
# C_transpose = C.T  # Transpose of the result matrix

# # Display results
# print("\nMatrix A:")
# print(A)
# print("\nMatrix B:")
# print(B)
# print("\nMatrix multiplication (A * B):")
# print(C)
# print("\nTranspose of the result matrix:")
# print(C_transpose)












# # Pandas Examples

# import numpy as np

# # 1. Create a 5x5 identity matrix using NumPy
# identity_matrix = np.identity(5)
# print("1. Identity Matrix:")
# print(identity_matrix)

# # 2. Generate a random matrix of size 3x3 and calculate its determinant
# random_matrix = np.random.rand(3, 3)
# determinant = np.linalg.det(random_matrix)
# print("\n2. Random Matrix:")
# print(random_matrix)
# print("   Determinant:", determinant)

# # 3. Create a NumPy array of integers from 1 to 20 and reshape it into a 4x5 matrix
# array_1_to_20 = np.arange(1, 21)
# reshaped_array = array_1_to_20.reshape(4, 5)
# print("\n3. Reshaped Array:")
# print(reshaped_array)

# # 4. Find the eigenvalues and eigenvectors of a given square matrix
# # (Let's take the random matrix generated in question 2)
# eigenvalues, eigenvectors = np.linalg.eig(random_matrix)
# print("\n4. Eigenvalues:")
# print(eigenvalues)
# print("   Eigenvectors:")
# print(eigenvectors)

# # 5. Calculate the dot product of two given vectors
# vector1 = np.array(eval(input("Enter vector 1 as a list: ")))
# vector2 = np.array(eval(input("Enter vector 2 as a list: ")))
# dot_product = np.dot(vector1, vector2)
# print("\n5. Dot Product:", dot_product)

# # 6. Create a NumPy array with random values and replace positive values with 1 and negative values with -1
# random_array = np.random.randn(10)
# modified_array = np.where(random_array > 0, 1, -1)
# print("\n6. Modified Array:")
# print(modified_array)

# # 7. Calculate the inverse of a given matrix
# # (Let's use the random_matrix generated in question 2)
# inverse_matrix = np.linalg.inv(random_matrix)
# print("\n7. Inverse Matrix:")
# print(inverse_matrix)

# # 8. Calculate the cross product of two given vectors
# cross_product = np.cross(vector1, vector2)
# print("\n8. Cross Product:")
# print(cross_product)

# # 9. Create a NumPy array with elements ranging from 10 to 100 and extract all odd numbers
# start = int(input("Enter start of range: "))
# end = int(input("Enter end of range: "))
# array_10_to_100 = np.arange(start, end + 1)
# odd_numbers = array_10_to_100[array_10_to_100 % 2 != 0]
# print("\n9. Odd Numbers in Range:")
# print(odd_numbers)

# # 10. Calculate the cumulative sum of elements along a given axis of a NumPy array
# axis = int(input("Enter axis (0 for rows, 1 for columns): "))
# cumulative_sum = np.cumsum(reshaped_array, axis=axis)
# print("\n10. Cumulative Sum:")
# print(cumulative_sum)

# # import numpy as np

# # 11. Calculate the mean, median, and mode of a given array using NumPy
# array = np.array(eval(input("Enter array as a list: ")))
# mean = np.mean(array)
# median = np.median(array)
# mode = np.argmax(np.bincount(array))
# print("Mean:", mean)
# print("Median:", median)
# print("Mode:", mode)

# # 12. Compute the element-wise product of two given arrays using NumPy
# array1 = np.array(eval(input("Enter first array as a list: ")))
# array2 = np.array(eval(input("Enter second array as a list: ")))
# element_wise_product = np.multiply(array1, array2)
# print("Element-wise product:", element_wise_product)

# # 13. Create a 2D array with random integers and replace negative values with the mean of the array
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))
# random_array = np.random.randint(-10, 10, size=(rows, cols))
# mean_value = np.mean(random_array)
# random_array[random_array < 0] = mean_value
# print("Array with replaced negative values:")
# print(random_array)

# # 14. Calculate the determinant of a given square matrix using NumPy
# matrix = np.array(eval(input("Enter square matrix as a list of lists: ")))
# determinant = np.linalg.det(matrix)
# print("Determinant:", determinant)

# # 15. Normalize a given array using NumPy (scale the values between 0 and 1)
# array_to_normalize = np.array(eval(input("Enter array to normalize as a list: ")))
# normalized_array = (array_to_normalize - np.min(array_to_normalize)) / (np.max(array_to_normalize) - np.min(array_to_normalize))
# print("Normalized array:", normalized_array)

# # 16. Create a random 3x3 matrix and perform a matrix inversion operation using NumPy
# random_matrix = np.random.rand(3, 3)
# inverse_matrix = np.linalg.inv(random_matrix)
# print("Random Matrix:")
# print(random_matrix)
# print("Inverse Matrix:")
# print(inverse_matrix)

# # 17. Calculate the cross-correlation of two given 1D arrays using NumPy
# array1 = np.array(eval(input("Enter first 1D array as a list: ")))
# array2 = np.array(eval(input("Enter second 1D array as a list: ")))
# cross_correlation = np.correlate(array1, array2, mode='full')
# print("Cross-correlation:")
# print(cross_correlation)

# # 18. Find the k largest values and their indices in a given 1D array using NumPy
# array = np.array(eval(input("Enter 1D array as a list: ")))
# k = int(input("Enter the value of k: "))
# largest_indices = np.argsort(array)[-k:]
# largest_values = array[largest_indices]
# print("Indices of k largest values:", largest_indices)
# print("k largest values:", largest_values)

# # 19. Create a 3x3 matrix with random values and perform a singular value decomposition (SVD) using NumPy
# random_matrix = np.random.rand(3, 3)
# U, s, V = np.linalg.svd(random_matrix)
# print("Original Matrix:")
# print(random_matrix)
# print("U (left singular vectors):")
# print(U)
# print("S (singular values):")
# print(s)
# print("V (right singular vectors):")
# print(V)

# # 20. Calculate the cumulative product of elements along a given axis of a NumPy array
# array = np.array(eval(input("Enter array as a list: ")))
# axis = int(input("Enter axis (0 for rows, 1 for columns): "))
# cumulative_product = np.cumprod(array, axis=axis)
# print("Cumulative product:")
# print(cumulative_product)









