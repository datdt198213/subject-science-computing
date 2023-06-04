import math
import sympy as sp

def f(x):
    return math.sin(x)

# Tính giá trị đạo hàm của hàm fx tại điểm point 
def f_derivative(f, x, point):
    derivative = sp.diff(f, x).subs(x, point)
    print(f"\nĐạo hàm của f tại điểm x = {point} là: {derivative} \n")
    return derivative

def fx_sym(x):
    return sp.sin(x) 

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


x = sp.Symbol('x')
fx = fx_sym(x)
point = math.pi / 3
target_derivative = f_derivative(fx, x, point)
# target_derivative = math.cos(math.pi / 3)
optimal_h = None
target_approx = 0
min_error = float('inf')

# from 10 ** -1 to 10 ** -17
for k in range(1, 17):
    h = 10 ** -k
    approx_derivative = central_difference(f, math.pi / 3, h)
    error = abs(target_derivative - approx_derivative)
    
    if error < min_error:
        min_error = error
        optimal_h = h
        target_approx = approx_derivative
    
    print(f"h = {h:.16f}, Đạo hàm xấp xỉ = {approx_derivative:.16f}, Sai số = {error:.16f}")

print(f"\nOptimal h: {optimal_h}, Đạo hàm xấp xỉ: {target_approx}, Sai số: {min_error}")
