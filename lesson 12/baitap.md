### Bài tập:

#### I. Stack

I.1. Đảo ngược chuỗi
input: string S: 'abc123'
output: string S reverse: '321cba'

#### II. Queue

II.1. Tạo số nhị phân từ 1 đến N bằng cách sử dụng Hàng đợi
Cho một số dương N, tạo hiệu quả các số nhị phân từ 1 đến N bằng cách sử dụng cấu trúc dữ liệu hàng đợi và trong thời gian tuyến tính.
input: 16
output: 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000

Code mẫu

```python
def generate_binary_numbers(N):
    result = []
    queue = ["1"]  # Khởi tạo hàng đợi với phần tử đầu tiên là "1"

    for _ in range(N):
        current = queue.pop(0)  # Giống dequeue
        result.append(current)

        # Tạo và thêm 2 số nhị phân tiếp theo
        queue.append(current + "0")
        queue.append(current + "1")

        print(f"current: {current}")
        print(f"result: {result}")
        print(f"queue: {queue}")

    return result

# Test
N = 16
binary_list = generate_binary_numbers(N)
print(" ".join(binary_list))

```

#### III. Stack + Queue

Cho một hàng đợi (queue), đảo ngược k phần tử đầu tiên của hàng đợi. Phần còn lại giữ nguyên thứ tự.
Gợi ý:

- Dùng Stack để đảo ngược phần đầu.
- Dùng Queue để duy trì phần còn lại.

Code mẫu

```python
def reverse_first_k(queue, k):
    stack = []

    # Bước 1: Lấy k phần tử đầu cho vào stack (đảo ngược)
    for _ in range(k):
        stack.append(queue.pop(0))  # pop(0) lấy phần tử đầu hàng đợi

    # Bước 2: Đưa lại vào queue (phần đảo ngược)
    while stack:
        queue.append(stack.pop())  # pop() lấy phần tử cuối stack

    # Bước 3: Đưa phần còn lại từ đầu lên cuối để giữ nguyên thứ tự
    size = len(queue)
    for _ in range(size - k):
        queue.append(queue.pop(0))  # Đưa phần tử đầu ra cuối

    return queue

# Test
q = [1, 2, 3, 4, 5]
k = 3
result = reverse_first_k(q, k)
print(result)  # [3, 2, 1, 4, 5]
```
