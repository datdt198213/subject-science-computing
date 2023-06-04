import numpy as np

# Bộ dữ liệu mẫu
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 7, 9])

# Tạo ma trận A và vector b cho hồi quy phi tuyến
A = np.column_stack((x**2, x, np.ones_like(x)))
b = y

# Tìm nghiệm x bằng phương pháp hồi quy phi tuyến
x_hat = np.linalg.lstsq(A, b, rcond=None)[0]

# Trích xuất các tham số a, b, c từ nghiệm x
a = x_hat[0]
b = x_hat[1]
c = x_hat[2]

# In đường cong khớp
print("Đường cong khớp: y =", a, "* x^2 +", b, "* x +", c)