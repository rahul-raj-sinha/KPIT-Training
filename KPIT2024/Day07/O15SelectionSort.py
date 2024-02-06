def selection_sort(arr):
  for i in range(len(arr)):
    # Find the maximum element in the unsorted portion of the array
    max_index = i
    for j in range(i + 1, len(arr)):
      if arr[j] > arr[max_index]:
        max_index = j

    # Swap the maximum element with the first unsorted element
    arr[i], arr[max_index] = arr[max_index], arr[i]

  return arr


arr = [5, 3, 4, 2, 8, 6]
print(selection_sort(arr))