names = ["Tuan Anh", "Duc Nhn", "Hien Le", "Gia Binh"]
# index       0           1          2          3

# names[1] = "Duc Nhan" # truy cập phần tử theo index

# print(len(names)) # length - độ dài danh sách

# # Xóa phần tử
# del names[1] # xóa theo index
# names.remove("Tuan Anh") # xóa theo value

# # Thêm phần tử
# names.append("Nguyen Van A") # thêm phần tử vào cuối list
# names.insert(2, "Pham Van B") # thêm phần tử vào vị trí chỉ định
# print(names)

# Duyệt phần tử của một list
# Duyệt không quan tâm tới chỉ số, chỉ quan tâm giá trị phần tử
for name in names:
    print(name)

# Cần quan tâm tới chỉ số
for i in range(len(names)): # 0 1 2 3
    print(i+1, end=". ")
    print(names[i])