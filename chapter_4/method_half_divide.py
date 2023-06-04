import math


def f(x):
    # Định nghĩa hàm f(x) của phương trình

    #sign(x-2) * sqrt(|x - 2|) = 0
    # return math.copysign(1, x-2) * math.sqrt(abs(x))

    # e**x - 2 = 0
    return math.e**x - 2


def bisection_method(a, b, epsilon):
    # Phương pháp chia đôi
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    epsilon_result = b - a
    print("Sai số cuối cùng của hàm là: ", epsilon_result)
    return (a + b) / 2

# Thực hiện giải phương trình bằng phương pháp chia đôi
a = 0
b = 2
epsilon = 0.01
root = bisection_method(a, b, epsilon)

print("Nghiệm của phương trình là:", root)
print("Giá trị tại ngiệm của phương trình là:", f(root))