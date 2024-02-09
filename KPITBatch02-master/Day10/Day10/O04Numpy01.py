import numpy as np
# List
arr = np.array([1, 2, 3, 4, 5])
print(f"arr :{arr}")
print(type(arr))

# tuple
arr1 = np.array(('a', 'b', 'c', 'd'))
print(f"arr1 :{arr1}")
print(type(arr1))

print("-" * 60)
# dimension
arr2 = np.array(50)
print(f"arr2 :{arr2}")
print("-" * 60)
# one dimension
arr3 = np.array([1, 2, 3, 4, 5])
print(arr3)
print("-" * 60)
# two dimension
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4)
print("-" * 60)
# three dimensipn

arr5 = np.array([[[1, 2, 3],
                  [4, 5, 6]],
                 [[7, 8, 9],
                  [10, 11, 12]]])
print(f"arr5 :{arr5}")
print("-" * 60)
print(f"arr2 :{arr2.ndim}")
print("-" * 60)
print(f"arr3 :{arr3.ndim}")
print("-" * 60)
print(f"arr4 :{arr4.ndim}")
print("-" * 60)
print(f"arr5 :{arr5.ndim}")

print("-" * 60)
arr6 = np.array([1, 2, 3, 4,5], ndmin=5)
print(f"arr5 :{arr6}")
print(f"arr6 :{arr6.ndim}")

print("-" * 60)
arr7 = np.zeros((2, 3))
print(f"arr7: {arr7}")

print("-" * 60)
arr8 = np.zeros((2, 3, 4))
print(f"arr8 :{arr8}")

print("-" * 60)
arr9 = np.identity(3)
print(arr9)
