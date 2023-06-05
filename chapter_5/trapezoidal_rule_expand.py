import math

def f(x):
    # f = sin(x)
    # return math.sin(x)
    # f = 1 / (1 + x*x)
    # if x != 0:
    #     f = math.sin(x) / x
    # else: 
    #     f = 1
    # f = x*x*x*x + 2*x*x*x + 1
    # f = 1/ (1 + x*x)
    f = 1 / x
    return f

def trapezoidal_rule_expand(f, a, b, n):
    h = (b - a) / n
    loop_value = 0
    integral = 0
    print(f"h = {h}")

    for i in range(1, n):
        loop_value += round(f(a + i * h), 6)
        print(f"loop value = {loop_value} at f(a = {a} + i = {i} * h = {h}) = {f(a + i * h)}")
    
    integral = h/2 * (f(a) + 2 * loop_value + f(b))
    print(f"\nIntegral = {integral} at loop value = {loop_value}")
    return integral

a = 1  # Giới hạn dưới của khoảng tích phân
b = 5  # Giới hạn trên của khoảng tích phân
n = 4  # Số lượng đoạn chia

approx_integral = trapezoidal_rule_expand(f, a, b, n)

print(f"Approximate integral: {approx_integral:.6f}")
# print(f"Exact integral: {exact_integral:.6f}")
# print(f"Error: {error:.6f}")