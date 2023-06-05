#
#Tính gần đúng đạo hàm theo công thức sai phân thuận
#

import math
import sympy as sp


"""
f_symbol: hàm fx với x là symbol 
x: Ký hiệu x trong thư viện sympy
point: Giá trị của x ta muốn tính đạo hàm
return: giá trị đạo hàm tại điểm point
"""
def f_derivative(f_symbol, x, point):
    derivative = sp.diff(f_symbol, x).subs(x, point)
    print("\nĐạo hàm của f tại điểm x =", point, "là:", derivative, "\n")
    return derivative

"""
Tính giá trị hàm f tại điểm x
x: giá trị muốn tính hàm f tại điểm đó
return: giá trị của hàm f tại x
"""
def f(x):
    # return math.sin(x)
    # return x * ((math.cos(2.3*x))**(1/3))
    # return x*x*x*x + 2*x*x*x -x + 1
    return math.cos(x)

"""
Chuyển hàm fx sang dạng sym để  thực hiện tính đạo hàm
x: Ký hiệu x trong thư viện sympy 
return: hàm fx với x là ký tự 
"""
def fx_sym(x):
    # return sp.sin(x)
    # return x * ((sp.cos(2.3*x))**(1/3)) 
    # return x*x*x*x + 2*x*x*x -x + 1
    return sp.cos(x)

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def main():
    x = sp.Symbol('x')
    fx = fx_sym(x)
    # point = math.pi / 3
    point = 1
    target_derivative = f_derivative(fx, x, point)

    # target_derivative = math.cos(math.pi / 3)
    optimal_h = None
    target_approx = 0
    min_error = float('inf')

    for k in range(1, 17):
        h = 10 ** -k
        # approx_derivative = forward_difference(f, math.pi / 3, h)
        approx_derivative = forward_difference(f, point, h)
        error = abs(target_derivative - approx_derivative)
        
        if error < min_error:
            min_error = error
            optimal_h = h
            target_approx = approx_derivative
        
        print(f"h = {h:.16f}, Đạo hàm xấp xỉ = {approx_derivative:.16f}, Sai số = {error:.16f}")

    print(f"\nOptimal h: {optimal_h}, Đạo hàm xấp xỉ: {target_approx}, Sai số: {min_error}")

main()