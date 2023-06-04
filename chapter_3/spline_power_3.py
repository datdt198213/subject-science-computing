import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Dữ liệu ví dụ
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
power = np.array([54.4, 54.6, 67.1, 78.3, 85.3, 88.7, 96.9, 97.6, 84.1, 80.1, 68.8, 61.1])

# Xây dựng spline bậc 3 từ dữ liệu
spline = CubicSpline(hours, power)

# Tạo dữ liệu để vẽ đồ thị nội suy
x = np.linspace(hours.min(), hours.max(), 200)
y = spline(x)

# Vẽ đồ thị nội suy
plt.plot(hours, power, 'o', label='Dữ liệu thực tế')
plt.plot(x, y, label='Spline bậc 3')
plt.xlabel('Giờ')
plt.ylabel('Công suất')
plt.title('Nội suy spline bậc 3')
plt.legend()
plt.show()