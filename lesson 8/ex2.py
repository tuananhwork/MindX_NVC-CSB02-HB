# Xác định IPO:
# I: balls
# O: balls_sorted
# P: ...
def balls_sorted_app(balls: list):
    # Tìm số lượng bóng mỗi loại
    count_r = balls.count('r') # 4
    count_w = balls.count('w') # 2
    count_b = balls.count('b') # 3

    # Khái niệm cộng mảng, nhân mảng:
    # [a, b] + [c, d] = [a, b, c, d]
    # [a, b] * 2 = [a, b, a, b]
    #################################

    balls_sorted = ['r'] * count_r + ['w'] * count_w + ['b'] * count_b
    return balls_sorted

balls = ['r', 'w', 'r', 'b', 'w', 'b', 'r', 'r', 'b']

print(balls_sorted_app(balls))