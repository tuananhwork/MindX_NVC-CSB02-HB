import random
arr = random.sample(range(10), 5)

def insertion_sort(arr):
    arr_sorted = []
    while arr:
        minimum = min(arr)
        arr_sorted.append(minimum)
        arr.remove(minimum)
    return arr_sorted

arr_sorted = insertion_sort(arr)