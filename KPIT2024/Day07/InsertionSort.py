def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_item
        print(arr)

arr = [8, 12, 5, 9, 6, 3, 7]
insertion_sort(arr)
print(arr)