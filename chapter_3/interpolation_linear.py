# Thay giá trị tại điểm x = 4 vào các phương trình trong đáp án
# Nếu thấy bằng với result thì chọn
# Trong trường hợp có 2 kết quả thì thay đổi x là một giá trị khác và thử lại

import numpy as np

def lagrange_interpolation(x, y, xi):
    n = len(x)
    yi = 0.0

    for i in range(n):
        l = 1.0
        for j in range(n):
            if j != i:
                l *= (xi - x[j]) / (x[i] - x[j])
        yi += y[i] * l

    return yi

# Example data
x = np.array([0, 0.25, 0.5, 0.75, 1])
y = np.array([1, 2 ** 0.25, 2 ** 0.5, 2 ** 0.75, 2])

# Interpolate at a specific point
xi = 0.45
yi = lagrange_interpolation(x, y, xi)

print("Interpolated value at xi =", xi, "is yi =", yi)