import assignment_module.factorial as fac
import assignment_module.fibonacci as fib
import assignment_module.sorting as srt

# print(fac.fact(5))
# for i in range(5):
#     print(fib.Fib(i), end=" ")

print(srt.bubble_sort([1, 3, 5, 4, 2]))

arr = [1, 4, 5, 3, 2]
srt.heap_sort(arr)
print(arr)

print(srt.insertion_sort([1, 5, 4, 3, 2]))
print(srt.quick_sort([1, 5, 4, 3, 2]))
