import numpy as np
from scipy.interpolate import CubicSpline

# Bộ dữ liệu mẫu
x = np.array([1, 2, 3])
y = np.array([3.5, 6, 10.5])

# Tạo đối tượng nội suy spline
spline = CubicSpline(x, y)

# Giá trị x mới để nội suy
x_new = np.linspace(1, 3, 100)  # Tạo một dãy giá trị x trong khoảng từ 1 đến 3

# Tính giá trị y tương ứng thông qua nội suy
y_new = spline(x_new)

# In kết quả
for i in range(len(x_new)):
    print("Nội suy tại x =", x_new[i], ": y =", y_new[i])