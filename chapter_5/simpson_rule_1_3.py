def f(x):
    # return x**2 + 1
    return 1 / (1 + x*x)

def simpson13(a, b, n):
    h = (b - a) / n
    x0 = a
    x1 = a + h
    x2 = b
    I = h / 3 * (f(x0) + 4 * f(x1) + f(x2))
    return I

# Example usage
a = 1
b = 5
n = 4
# n = 2 được sử dụng trong công thức simpson 1 / 3
result = simpson13(a, b, n)
print(result)