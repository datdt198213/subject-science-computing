def f(x):
    return 1 / (1 + x**2)

def simpson_3_8(a, b, n):
    h = (b - a) / n 
    sum = f(a) + f(b) # Tính tổng các đầu mút
    
    for i in range(1, n):
        if i % 3 == 0:
            sum += 2 * f(a + i * h)
        else:
            sum += 3 * f(a + i * h)
    
    integral = (3 * h / 8) * sum
    return integral

a = 0
b = 1
n = 8

result = simpson_3_8(a, b, n)
print(f"Giá trị gần đúng của phương trình tích phân: {result} ")