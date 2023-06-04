def f(x, y):
    return x + y

def runge_kutta2(f, x0, y0, h, n):
    """
    f: Hàm đại diện cho phương trình vi phân y' = f(x, y)
    x0: Giá trị ban đầu của x
    y0: Giá trị ban đầu của y tại x = x0
    h: Kích thước bước
    n: Số bước lặp
    """
    x = [x0]
    y = [y0]
    
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h, y[i] + k1)

        x_next = round(x[i] + h, 3)
        y_next = y[i] + 1/2 * (k1 + k2)
        x.append(x_next)
        y.append(y_next)
    
    return x, y

# Ví dụ: Giải phương trình vi phân y' = x + y với y(0) = 1
x0 = 0
y0 = 1
h = 0.1
n = 10

x, y = runge_kutta2(f, x0, y0, h, n)

# In kết quả
for i in range(len(x)):
    print(f"x = {x[i]}, y = {y[i]}")