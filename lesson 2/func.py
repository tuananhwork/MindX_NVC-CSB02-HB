def calc_median(ls: list):
    ls.sort() # sắp xếp danh sách từ nhỏ tới lớn
    print(ls)

    if (len(ls) % 2 == 1):
        mid = len(ls) // 2
        median = ls[mid]
    else:
        mid = len(ls) // 2 - 1
        median = ls[mid] + ls[mid + 1]
        median = median / 2
    
    return median

print(calc_median([1, 2, 4, 1, 5, 8, 9, 10]))
print(calc_median([1, 4, 1, 1, 6, 8, 9, 10]))



# Một số khái niệm khi làm việc với hàm
# Được coi là một chương trình con để tránh lặp lại code và rõ ràng cấu trúc chương trình
# Tham số: là biến được truyền vào hàm khi khai báo, trong ví dụ bên trên: list
# Đối số: là biến được truyền vào hàm khi gọi, trong ví dụ trên: [1, 2, 4, 1, 5, 8, 9, 10]
# Dùng keyword return khi muốn hàm trả về một giá trị nào đó sau khi kết thúc

