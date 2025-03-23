def linear_search(arr: list, num):
    for k in arr:
        if k == num:
            return True
    return False
# return True / False bởi vì chỉ cần kiểm tra phần tử có thuộc
# danh sách arr hay không, không cần lấy thông tin vị trí

def arr_intersect(arr1: list, arr2: list):
    arr1_ready = set(arr1) # Loại bỏ các phần tử trùng nhau trong arr
    arr2_ready = set(arr2)
    result = [] # Tạo mảng chứa danh sách các phần tử giao nhau
    for i in arr1_ready: # Lặp qua mảng thứ nhất
        if linear_search(arr2_ready, i): # Nếu tìm thấy phần tử nào cũng thuộc mảng thứ 2
            result.append(i) # Thì thêm phần tử đó vào danh sách result
    return result

# Ví dụ mảng:
arr1 = [1, 3, 2, 4, 3, 1, 1, 2, 5, 7]
arr2 = [5, 9, 4, 4, 1, 7, 8, 10, 200]
# -> result = [1, 4, 5, 7]

# Hiển thị danh sách phần tử giao nhau của 2 mảng
result = arr_intersect(arr1, arr2)
if not result:
    print('Khong co phan tu giao nhau trong arr1 va arr2')
else:
    print(f'Danh sach phan tu giao nhau: {result}')

# Giải thích nội dung thuật toán:
# - Sử dụng một trong hai thuật toán tìm kiếm đã học để xác định xem phần tử ở
# mảng thứ nhất có thuộc mảng thứ hai hay không (tìm phần tử ở mảng thứ nhất trong
# mảng thứ hai, nếu thấy trả về True, không thấy trả về False
# - Trước khi tìm kiếm, gọi hàm set() để loại bỏ đi các giá trị trùng lặp để tiết
# kiệm thời gian thực thi

