import numpy as np

arr1 = np.array([2, 3, 4])
print(arr1.ndim)
print(arr1.dtype)

print("-" * 60)
arr2 = np.array([-2, -1, 0, 1, 2])
print(arr2)
print(arr2.ndim)
print(arr2.dtype)

print("-" * 60)
arr3 = np.array([0.1, 0.2, 0.3])
print(arr3)
print(arr3.ndim)
print(arr3.dtype)

print("-" * 60)
arr4 = np.array([1, 2, 3, 4,5], dtype='int32')
print(arr4)
print(arr4.dtype)

print("-" * 60)
arr1 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
print(f"dimension :{arr1.ndim}")
print(f"size :{arr1.size}")
print(f"shape :{arr1.shape}")
print(f"itemsize :{arr1.itemsize}")
