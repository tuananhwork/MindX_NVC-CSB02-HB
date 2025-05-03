## Kiến thức Python cơ bản

#### Câu lệnh print: hiển thị dữ liệu ra màn hình
```python
print('Hello')
print(1000)
print(True)
```

#### Câu lệnh input: dùng để nhập giá trị từ bàn phím
```python
name = input("What's your name?")
```

#### Cú pháp comment: #
- dùng để ghi chú lại tác dụng, thuật toán một đoạn lệnh
- dùng để vô hiệu hóa một đoạn lệnh

#### Biến:
- Coi như một chỗ để chứa giá trị
- Trong python, không cần khởi tạo, chỉ cần gán giá trị cho biến
```C++
int count; // khởi tạo biến
count = 10; // gán giá trị cho biến
```

#### Các kiểu dữ liệu cơ bản
- số nguyên - int: 10, -5, 0, 100
- số thực - float: 3.4, 10.5, -0.7798
- xâu chuỗi - str: "Tuan Anh", "MindX"
- logic - bool: True, False

#### Các toán tử số học (áp dụng với kiểu dữ liệu int hoặc float)
```python
a = 101
b = 4
print(a+b)  
print(a-b)
print(a*b)
print(a/b)
print(a//b)   # Chia lấy phần nguyên
print(a%b)    # Chia lấy phần dư
print(a**b)   # Lũy thừa
```

#### Toán tử quan hệ
```python
a = 10
b = 4
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)
```

#### Toán tử logic
```python
a = 10
b = 4
c = 7
d = 1000
print(a < b and c >= d)  # False
print(a < b or c >= d)   # False
print(a > b and c <= d)  # True
print(a > b or c >= d)   # True
```

#### Cấu trúc rẽ nhánh if - elif - else
```python
if a > b:
    print("a is greater")
elif b > a:
    print("b is greater")
else:
    print("a and b is equal")
```

#### Cấu trúc lặp
```javascript
for (let i = 0; i < 10; i++) {
    console.log(i)
}
// 0 1 2 3 4 5 6 7 8 9
```
```python
# Vòng lặp for - biết trước số lần lặp
for i in range(10):
    print(i)
# 0 1 2 3 4 5 6 7 8 9

# Vòng lặp while - không biết trước số lần lặp
count = 0
while count < 10:
    print('Hello')
    count = count + 1
```

#### Chi tiết về hàm range()
- Hàm range tạo ra một danh sách số nguyên
- Có 3 cú pháp của hàm range, trong đó cú pháp tổng quát: range(start, end, step)
- Với trường hợp 1 tham số: range(n): Trả về danh sách [0, 1, 2, ..., n-1]
- Với trường hợp 2 tham số: range(a, b): Trả về danh sách [a, a+1, a+2, ..., b-1]
- Với trường hợp 3 tham số: range(a, b, x): Trả về danh sách [a, a+x, a+2x, ..., (trước b)]
Ví dụ:
range(1, 50, 13): [1, 14, 27, 40]