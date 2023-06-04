import numpy as np

def calculate_spline_coefficients(x, y):
    n = len(x) - 1
    h = np.diff(x)
    
    # Tính ma trận A
    A = np.zeros((n-1, n-1))
    for i in range(1, n):
        A[i-1, i-1] = (h[i-1] + h[i]) / 3
        if i < n-1:
            A[i-1, i] = h[i] / 6
        if i > 1:
            A[i-1, i-2] = h[i-1] / 6
    
    # Tính vector B
    B = np.zeros((n-1, 1))
    for i in range(1, n):
        B[i-1] = ((y[i+1] - y[i]) / h[i]) - ((y[i] - y[i-1]) / h[i-1])
    
    # Giải hệ phương trình tuyến tính
    c = np.linalg.solve(A, B)
    
    # Tính các hệ số a, b, d
    a = y[:-1]
    b = np.zeros(n)
    d = np.zeros(n)
    for i in range(1, n):
        b[i] = (y[i+1] - y[i]) / h[i] - h[i] * (2 * c[i-1] + c[i]) / 6
        d[i] = (c[i] - c[i-1]) / h[i]
    
    return a, b, c, d

# Dữ liệu ví dụ
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
y = np.array([2, 3, 5, 4, 6, 8, 7, 9, 10, 12, 11, 13])

# Tính toán các hệ số
a, b, c, d = calculate_spline_coefficients(x, y)

# In các hệ số
for i in range(len(a)):
    print(f"a[{i}] = {a[i]}, b[{i}] = {b[i]}, c[{i}] = {c[i]}, d[{i}] = {d[i]}")