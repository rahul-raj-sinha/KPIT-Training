
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

print("-" * 60)

arr1 = np.array((10,20,30, 40, 50))
print(f"arr1 :{arr1}")
print(type(arr1))

print("-" * 60)
# dimensions
arr = np.array(50)
print(f"arr :{arr}")
print(type(arr))

print("-" * 60)
arr0 = np.array(100)
arr1 = np.array([1, 2, 3,4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[8, 9, 10], [11, 12, 13]]])

print(f"arr0 :{arr0} \t {arr0.ndim}-dimension")
print(f"arr1 :{arr1} \n {arr1.ndim}-dimension")
print(f"arr2 :{arr2} \n {arr2.ndim}-dimension")
print(f"arr3 :{arr3} \n {arr3.ndim}-dimension")

print("-" * 60)

arr4 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr4)

print(type(arr4))
