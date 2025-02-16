from animal import Animal

dog = Animal("Dog", "Brown")
cat = Animal("Cat", "Orange")
# ... có thể tạo vô số đối tượng từ một lớp

cat.type = "Tiger" # Truy cập và câp nhật thuộc tính đối tượng
cat.className = "Cat"

print(cat.className)
print(dog.className)