n = int(input("Enter an integer: "))

sum = 0
for i in range(n+1): # O(n)
    sum += i

sum = (1 + n) * n / 2 # O(1)

Độ phức tạp: O(n)

Chạy n + 1 lần:
lần đầu: i = 0
lần 2: i = 1
...
lần n: i = n

O(n+1) -> O(n)

f(n) = n + 9*9999999
n = 10 -> f(n) = 11
limit: n = 10^1000 -> f(n) = n


for i in range(n): # O(n^2)
    for j in range(n):
        print(f'{i}, {j}')


O(1)
O(log(n))
O(n)
O(nlog(n))
O(n^2)
O(n!)
