## OOP - Oriented Object Programing
1. Đối tượng
- Đối tượng (object): Là thực thể có các trạng thái và hành vi, hay còn gọi là thuộc tính (biến) và phương thức (hàm)
Ví dụ:
- Đối tượng xe BWM là một object:
  + Thuộc tính: màu trắng, 4 bánh, 4 chỗ
  + Phương thức: đi tiến, đi lùi, rẽ, bốc đầu
2. Lớp
- Lớp (class): Là bản thiết kế để tạo ra đối tượng. Lớp sẽ định nghĩa các thuộc tính và phương thức của đối tượng. Khi tạo một đối tượng từ lớp, đối tượng đó sẽ có tất cả các đặc điểm do lớp quy định

## Các tính chất của OOP
### Tính đóng gói - Encapsulation: ẩn thông tin bên trong đối tượng, cho phép truy cập dữ liệu theo cách được kiểm soát
- Lợi ích: 
  + Bảo vệ dữ liệu
  + Kiểm soát truy cập: thông qua các phương thức được định nghĩa trước
  + Dễ bảo trì, mở rộng
- Một số lưu ý
  + Mặc định tất cả các thuộc tính và phương thức đều public, có thể truy cập và thay đổi từ bên ngoài
  + Quy ước: đặt 1 dấu _ trước tên biến (_attribute) protected, vẫn có thể truy cập được từ bên ngoài nhưng không nên làm vậy. Đặt 2 dấu _ trước tên biến (__attribute) private sẽ không thể truy cập từ bên ngoài

### Tính kế thừa - Inheritance: