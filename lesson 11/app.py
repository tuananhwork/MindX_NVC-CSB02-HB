stack = [1, 2, 3] # Tạo ngăn xếp

# Kiểm tra ngăn xếp rỗng
if not stack:
    print('Empty')
else:
    print('Not empty')

# Thêm phần tử vào ngăn xếp
stack.append(4) # Stack = [1, 2, 3, 4]

# Lấy phần tử ở đầu ngăn xếp (Làm thay đổi stack)
stack.pop() # Stack = [1, 2, 3]

top = stack[-1] # Không làm thay đổi stack, Stack = [1, 2, 3, 4]

