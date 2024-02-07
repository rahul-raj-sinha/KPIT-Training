import numpy as np
arr1 = np.array([2, 3, 4])
print(arr1)
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
print(np.dtype)
print("-" * 60)
arr4 = np.array([1, 2, 3, 4, 5], dtype='int32')
print(arr4)
print(arr4.dtype)
print("-" * 60)
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"dimension: {arr1.ndim}")
print(f"size: {arr1.size}")
print(f"shape: {arr1.shape}")
print(f"itemsize: {arr1.itemsize}")
 









import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(f"arr: {arr}")
print(type(arr))
print("-" * 60)
arr1 = np.array(('a', 'b', 'c', 'd'))
print(f"arr1: {arr1}")
print(type(arr1))
print("-" * 60)
# dimension
arr2 = np.array(20)
print(f"arr2: {arr2}")
print(type(arr2))
print()
print("-" * 60)
# one dimension
arr3 = np.array([1, 2, 3, 4, 5])
print(f"arr3: {arr3}")
print(arr3)
print("-" * 60)
# two dimension
arr4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print(arr4)
print(type(arr4))
print("-" * 60)
# three dimension
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"arr5: {arr5}")
print(type(arr5))
print(f"arr2: {arr2.ndim}")
print("-" * 60)
print(f"arr3: {arr3.ndim}")
print("-" * 60)
print(f"arr4: {arr4.ndim}")
print("-" * 60)
print(f"arr5: {arr5.ndim}")
print("-"*60)
arr6 = np.array([1,2,3,4,5], ndmin=5)
print(f"arr6: {arr6}")
print(f"arr6: {arr6.ndim}")
print("-"*60)
arr7 = np.zeros((2,3))
print(f"arr7: {arr7}")
print("-"*60)
arr8 = np.zeros((2,3,4))
print(f"arr8: {arr8}")
print("-"*60)
arr9 = np.identity(3)
print(f"arr9: {arr9}")
