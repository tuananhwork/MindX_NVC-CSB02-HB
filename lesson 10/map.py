'''
Ánh xạ: A -> B qua 1 function, áp dụng lên 1 list hoặc 1 set
map(function, itertable)

Trong môn toán: Ánh xạ được hiểu là biến đổi một giá trị thông qua một hàm số
ví dụ: f(x) = x^2 + 1
2 -> 5
7 -> 50
Trong lập trình: Ánh xạ được hiểu là biến đổi một giá trị thông qua một quy tắc nào đó (thường là một function được định nghĩa)
def square_x(x):
    return x**2
square(2) -> 4
square(5) -> 25
'''

gpa_10 = [7, 9, 10, 8, 5, 8] # gpa_4 = ?

gpa_4 = map(lambda x: x/10 * 4, gpa_10)

print(list(gpa_4))

'''
Dictionary:
user = {
    name: 'Tuan Anh',
    age: 22,
    school: 'HUST'
}
dict hoạt động dựa trên ánh xạ: key ---mapping---> value
Các thao tác trên dict:
    print(student["name"])       # Truy cập
    student["age"] = 21          # Cập nhật
    student["major"] = "IT"      # Thêm mới

for key in student:
    print(key, student[key])

# Hoặc
for key, value in student.items():
    print(key, value)
'''