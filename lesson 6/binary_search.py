# Đoán 1 số từ 1 - 100: 24
# 1. Nhân: 21 nhỏ hơn
# 2. Lê: 50 lớn hơn
# 3. Bình: 40 lớn hơn
# 4. Nhân: 35 Lớn hơn
# 5. Lê: 26 lớn hơn
# 6. Bình: 23 nhỏ hơn
# 7. Nhân: 24


# arr = [1, 9, 5, 8, 10, 200, 47, 89], num = 8
arr_softed = [1, 5, 8, 9, 10, 47, 89, 200] # len = 8 phần tử
#Index        0, 1, 2, 3,  4,  5,  6,   7

def binary_search(arr: list, num):
    # Xác định khoảng tìm kiếm
    start = 0
    stop = len(arr) - 1 # = 8 - 1 = 7
    while start <= stop:
        mid = (start +  stop) // 2 # CHỈ SỐ của phần tử nằm giữa
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            stop = mid - 1
        elif arr[mid] < num:
            start = mid + 1
    return False


