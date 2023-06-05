import math


def f(x):

    #sign(x-2) * sqrt(|x - 2|) = 0
    # f = math.copysign(1, x-2) * math.sqrt(abs(x))

    # e**x - 2 = 0
    # f = math.e**x - 2

    f = x * x * x * x + 2 * x * x * x - 2
    return f


def bisection_method(a, b, epsilon):
    # Phương pháp chia đôi
    while (b - a) > epsilon:
        c = (a + b) / 2
        print(f"a = {a}, c = {c}, b = {b}, epsilon = {b - a}")
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print(f"a = {a}, c = {c}, b = {b}, epsilon = {b - a}")
    if (b == c): return a 
    elif (a == c): return b

# Thực hiện giải phương trình bằng phương pháp chia đôi
a = 4
b = 10
epsilon = 0.00001
root = bisection_method(a, b, epsilon)

print("Nghiệm của phương trình là:", root)
print("Sai số thực tế:", f(root))