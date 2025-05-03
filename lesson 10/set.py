'''
Khai niem:
- là tập hợp các phần tử KHÔNG TRÙNG LẶP và KHÔNG CÓ THỨ TỰ
- dùng khi muốn lưu trữ những giá trị duy nhất
'''

# Khai báo
my_set = {1, 2, 3, 4}
empty_set = set() # không dùng = {} vì bị nhầm với dict
print(type(my_set))
'''
Các phép toán với tập hợp:
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Hợp: {1, 2, 3, 4, 5} - union: cộng
print(a & b)   # Giao: {3} - intersection: nhân
print(a - b)   # Hiệu: {1, 2} - difference: trừ
print(a ^ b)   # Phần tử không chung: {1, 2, 4, 5} - subset

Thêm, xóa phần tử:
a.add(6) # Thêm phần tử
a.update({1, 2, 3, 4}) # Thêm tập hợp
a.remove(2)  # Gây lỗi nếu không có phần tử
a.discard(7) # Không lỗi nếu phần tử không tồn tại
'''