# Độ phức tạp của thuật toán Big O

Độ phức tạp của thuật toán Big O là một cách để mô tả hiệu suất của một thuật toán, đặc biệt là thời gian và không gian mà nó sử dụng. Nó giúp chúng ta hiểu được cách mà thời gian thực thi của một thuật toán thay đổi khi kích thước đầu vào tăng lên.

## Các loại độ phức tạp phổ biến

1. **O(1) - Độ phức tạp hằng số**: Thời gian thực thi không thay đổi bất kể kích thước đầu vào.

   - **Ví dụ**: Truy cập một phần tử trong danh sách theo chỉ số.

   ```python
   def get_first_element(lst):
       return lst[0]  # O(1)
   ```

2. **O(n) - Độ phức tạp tuyến tính**: Thời gian thực thi tăng tuyến tính với kích thước đầu vào.

   - **Ví dụ**: Tính tổng các phần tử trong danh sách.

   ```python
   def sum_elements(lst):
       total = 0
       for num in lst:  # O(n)
           total += num
       return total
   ```

3. **O(n^2) - Độ phức tạp bậc hai**: Thời gian thực thi tăng theo bình phương kích thước đầu vào.

   - **Ví dụ**: Sắp xếp nổi bọt (Bubble Sort).

   ```python
   def bubble_sort(arr):
       n = len(arr)
       for i in range(n):  # O(n)
           for j in range(0, n-i-1):  # O(n)
               if arr[j] > arr[j+1]:
                   arr[j], arr[j+1] = arr[j+1], arr[j]  # O(1)
   ```

4. **O(log n) - Độ phức tạp logarithmic**: Thời gian thực thi tăng theo logarit của kích thước đầu vào.
   - **Ví dụ**: Tìm kiếm nhị phân (Binary Search).
   ```python
   def binary_search(arr, target):
       left, right = 0, len(arr) - 1
       while left <= right:  # O(log n)
           mid = (left + right) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               left = mid + 1
           else:
               right = mid - 1
       return -1
   ```

## Tại sao Big O quan trọng?

- **Đánh giá hiệu suất**: Giúp lập trình viên đánh giá và so sánh hiệu suất của các thuật toán khác nhau.
- **Tối ưu hóa**: Giúp xác định các điểm cần tối ưu hóa trong mã nguồn.
- **Dự đoán**: Giúp dự đoán cách mà thuật toán sẽ hoạt động với các kích thước đầu vào lớn hơn.

## Kết luận

Hiểu về độ phức tạp của thuật toán Big O là rất quan trọng trong lập trình và phát triển phần mềm, vì nó giúp bạn viết mã hiệu quả hơn và tối ưu hóa hiệu suất của ứng dụng.
