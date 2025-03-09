def linear_search(arr: list, num):
    # Duyệt từng phần tử của arr, nếu == num thì đưa ra chỉ số, kết thúc
    # Nếu != 5 thì chuyển tới phần tử kế tiếp
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

# Vi du: arr = [1, 9, 5, 8, 10, 200, 47, 89], num = 8
# i       arr[i]      arr[i] == num ?
# 0       1           False
# 1       9           False
# 2       5           False
# 3       8           True
# Kết thúc, hàm trả về 3

arr = [1, 9, 5, 8, 10, 200, 47, 89]
num = 8

print(linear_search(arr, num))
