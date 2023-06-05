import math

def f(x):
    # f = math.sin(x)
    # f = x*x*x*x + 2*x*x*x + 1
    f = 1/ (1 + x*x)
    return f
    

def trapezoidal_rule(f, a, b):
    h = (b - a) / 2
    integral = (f(a) + f(b)) * h 
    
    return integral

a = 1  # Giới hạn dưới của khoảng tích phân
b = 2 # Giới hạn trên của khoảng tích phân

approx_integral = trapezoidal_rule(f, a, b)
# exact_integral = 1 - math.cos(math.pi / 3)
# error = abs(exact_integral - approx_integral)

print(f"Approximate integral: {approx_integral:.6f}")
# print(f"Exact integral: {exact_integral:.6f}")
# print(f"Error: {error:.6f}")