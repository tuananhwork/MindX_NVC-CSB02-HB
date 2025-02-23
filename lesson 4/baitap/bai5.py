while True:
    n = int(input("Enter an integer number n (10 < n < 100): "))
    if 10 < n < 100:
        break
    print("Invalid value, please try again!")

# Cách dễ hiểu (C1)
resultA = 0
for i in range(1, n + 1):
    resultA += i

# Cách viết ngắn gọn hơn (C2)
resultA = sum(range(1, n + 1))

# C1
resultB = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        resultB -= i
    else:
        resultB += i
        
# C2 
resultB = sum(i if i % 2 == 1 else -i for i in range(n + 1))

# C1
resultC = 0
for i in range(1, n + 1):
    resultC += 1/i

# C2
resultC = sum(1/i for i in range(1, n + 1))

# C1
resultD = 0
for i in range(1, n + 1):
    resultD += pow(2, i)

# C2
resultD = sum(2**i for i in range(1, n + 1))

# Giai thừa của n, ký hiệu là n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
resultE = 1
for i in range(1, n + 1):
    resultE *= i

# Số nguyên tố là số lớn hơn 1, chỉ chia hết cho 1 và chính nó
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 1/2 + 1)):
        if number % i == 0:
            return False
    return True

# C1
prime_list = []
for i in range(1, n + 1):
    if is_prime(i):
        prime_list.append(i)
resultF = sum(prime_list)

# C2
resultF = sum(i for i in range(1, n + 1) if is_prime(i))