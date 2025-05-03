# Tính đa hình - Tính trừu tượng (OOP)

## Tính đa hình - Polymorphism

1. Khái niệm

- Đa hình (Polymorphism) là khả năng một phương thức hoặc toán tử có thể hoạt động trên nhiều kiểu dữ liệu hoặc lớp khác nhau.
- Lợi ích của đa hình:

  - Viết mã linh hoạt hơn, có thể xử lý nhiều loại đối tượng mà không cần biết chính xác kiểu dữ liệu của chúng.
  - Dễ mở rộng, thêm lớp mới mà không cần thay đổi code cũ.
  - Tăng tính trừu tượng, làm cho code dễ đọc và dễ bảo trì hơn.

- Có 3 cách thể hiện đa hình trong Python:
  - Đa hình qua phương thức chung (Method Overriding)
  - Đa hình qua nạp chồng toán tử (Operator Overloading)
  - Đa hình qua Duck Typing

2. Ví dụ

```python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Cow(Animal):
    def sound(self):
        return "Moo"

def make_sound(animal: Animal):
    print(animal.sound())

dog = Dog()
cat = Cat()
cow = Cow()

make_sound(dog)  # Output: Woof
make_sound(cat)  # Output: Meow
make_sound(cow)  # Output: Moo
```

## Tính trừu tượng - Abstraction

1. Khái niệm

- Tính trừu tượng (Abstraction) là khả năng ẩn đi các chi tiết cụ thể và chỉ hiển thị những gì cần thiết. Nó giúp giảm bớt sự phức tạp bằng cách chỉ tập trung vào những khía cạnh quan trọng của đối tượng.

- Lợi ích của tính trừu tượng:

  - Giảm sự phức tạp của hệ thống bằng cách ẩn đi các chi tiết không cần thiết.
  - Tăng tính bảo mật bằng cách che giấu các thông tin nhạy cảm.
  - Dễ dàng bảo trì và mở rộng hệ thống.

2. Ví dụ
