sample_arr = [1,3,2,4,5]

# [1, 2, 3, 4, 5, 6, 7, 8, 9]

def modify_bubble_sort(arr: list):
    for i in range(len(arr)):
        swapped = False
        print(f"Lan lap thu {i+1}")
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sample_arr_sorted = modify_bubble_sort(sample_arr)
print(sample_arr)