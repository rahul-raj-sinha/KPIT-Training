def selection_sorting(arr):
    n= len(arr)
    for i in range (n):
        min_index = i
        for j in range (i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i],arr[min_index] = arr[min_index],arr[i]

#input_sort= input("enter the numbers to get sorted :")
numbers = [21,12,10,-5,-3]
selection_sorting(numbers)
print(f"the sorted array:{numbers}")
