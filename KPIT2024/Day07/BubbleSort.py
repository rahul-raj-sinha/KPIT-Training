
def buble_sort(arr):
    print(arr)
    for j in range(len(arr)):
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
               arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                continue

arr = [7, 3, 9, 2, 6, 4]
buble_sort(arr)

print(f"arr :{arr}")
