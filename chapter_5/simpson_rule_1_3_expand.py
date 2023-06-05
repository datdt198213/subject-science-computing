import math

def f(x):
    # return 1 / (1 + x**2)
    # if x != 0:
    #     return math.sin(x) / x
    # else:
    #     return 1
    return 1 / ( 1 + x*x)

def simpson_rule(a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            sum += 2 * f(x)
        else:
            sum += 4 * f(x)
    integral = (h / 3) * sum
    return integral

a = 1  # Điểm bắt đầu của đoạn tích phân
b = 5  # Điểm kết thúc của đoạn tích phân
n = 4  # Số đoạn chia

approximation = simpson_rule(a, b, n)
print("Gần đúng giá trị của I: ", approximation)