grades = [9, 10, 6, 7, 8, 4, 9, 10, 6, 1000, 6]
# index   0  1   2  3  4  5  6   7  8   9    10

# Tính trung bình: mean
# mean = sum(grades) / len(grades)
# print(mean)

# Tính trung vị: median
grades.sort() # sắp xếp danh sách từ nhỏ tới lớn
print(grades)

if (len(grades) % 2 == 1):
    mid = len(grades) // 2
    median = grades[mid]
else:
    mid = len(grades) // 2 - 1
    median = grades[mid] + grades[mid + 1]
    median = median / 2

# print(median)

# Tính yếu vị: mode
grades_sort = grades.sort() 
# [4, 6, 6, 7, 8, 9, 9, 10, 10, 1000]

print(grades_sort)

# grade = grades_sort[0] # 4

mods = []

max = 0

# for i in range(len(grades_sort)): # 0 -> 9
#     count = 0
#     for j in range(i, len(grades_sort)):
#         if grades_sort[j] == grades_sort[i]:
#             count = count + 1 # Chưa khẳng định được đâu là mod
#     if (max < count): max = count
    
# print(max)