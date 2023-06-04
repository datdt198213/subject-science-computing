import numpy as np
from scipy.interpolate import CubicSpline

# Các giá trị x và y
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = np.array([54.4, 54.6, 67.1, 78.3, 85.3, 88.7, 96.9, 97.6, 84.1, 80.1, 68.8, 61.1])

# Xây dựng spline bậc 3
spline = CubicSpline(x, y)

# Tạo một mảng các giá trị x mới trong khoảng từ x[0] đến x[-1]
x_new = np.linspace(x[0], x[-1], 100)

# Lấy giá trị y tương ứng cho các giá trị x mới bằng spline
y_new = spline(x_new)

# In ra các giá trị x và y
for i in range(len(x_new)):
    print(f"x = {x_new[i]}, y = {y_new[i]}")