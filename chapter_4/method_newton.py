import math
from scipy.optimize import fsolve

def f(x):
    # Hàm f(x) đại diện cho phương trình cần giải
    # return x**2 - 4
    # return x*x - 4 * math.sin(x)
    return x * x - 2

def f_prime(x):
    # Hàm f_prime(x) đại diện cho đạo hàm của hàm f(x)
    # return 2*x - 4 * math.cos(x)
    return 2 * x

def newton_method(x0, tol, max_iter):
    # x0 là điểm bắt đầu gần đúng
    # tol là sai số cho phép
    # max_iter là số lần lặp tối đa
    x = x0
    for i in range(max_iter):
        fx = f(x)
        print(f"Vong lap {i + 1}: x = {x}, fx = {fx}")
        if abs(fx) < tol:  # Kiểm tra điều kiện dừng khi đạt đến sai số cho phép
            return x
        fx_prime = f_prime(x)
        if fx_prime == 0:  # Kiểm tra trường hợp phương trình không hội tụ
            return None
        x = x - fx / fx_prime  # Công thức Newton-Raphson
    return None  # Trường hợp không tìm được nghiệm sau số lần lặp tối đa

# Sử dụng phương pháp Newton để giải phương trình f(x) = 0 với điểm bắt đầu gần đúng x0 = 2, sai số cho phép 0.0001, số lần lặp tối đa 100
# x0 = 3
result = newton_method(4, 0.0001, 100)
if result is not None:
    print("Nghiệm xấp xỉ của phương trình là:", result)
    print("Sai số thực tế là", f(result))
else:
    print("Không tìm được nghiệm sau số lần lặp tối đa.")