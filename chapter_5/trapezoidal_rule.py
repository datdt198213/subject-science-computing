import math

def f(x):
    # f = sin(x)
    return math.sin(x)

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    
    integral *= h
    return integral

a = 0  # Giới hạn dưới của khoảng tích phân
b = math.pi / 3  # Giới hạn trên của khoảng tích phân
n = 5  # Số lượng đoạn chia

approx_integral = trapezoidal_rule(f, a, b, n)
# exact_integral = 1 - math.cos(math.pi / 3)
# error = abs(exact_integral - approx_integral)

print(f"Approximate integral: {approx_integral:.6f}")
# print(f"Exact integral: {exact_integral:.6f}")
# print(f"Error: {error:.6f}")