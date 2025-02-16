from statistics import mean, median, multimode

def calc_data(ls: list):
    mean_value = mean(ls)
    median_value = median(ls)
    multimode_value = multimode(ls)

    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Multimode: {multimode_value}")

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = [100, 200, 300, 400, 500]

calc_data(list1)
calc_data(list2)
calc_data(list3)
