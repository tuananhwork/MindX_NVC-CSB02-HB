import statistics # làm việc với thống kê

grades = [9, 10, 6, 7, 8, 4, 9, 9, 10, 6, 1000, 6]

mode = statistics.multimode(grades)
median = statistics.median(grades)

print(mode)
