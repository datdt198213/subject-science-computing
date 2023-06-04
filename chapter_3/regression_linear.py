import numpy as np

# Bộ dữ liệu mẫu
x = np.array([2, 3, 4, 5, 6, 7])
y = np.array([3, 6, 8, 11, 13, 14])

# Tạo ma trận A và vector b cho hồi quy tuyến tính Ax = b
A = np.column_stack((x, np.ones_like(x)))
b = y

# Tìm nghiệm x bằng phương pháp hồi quy tuyến tính
x_hat = np.linalg.lstsq(A, b, rcond=None)[0]

# Trích xuất hệ số góc và hệ số tự do từ nghiệm x
slope = x_hat[0]
intercept = x_hat[1]

# In đường thẳng khớp
print("Đường thẳng khớp: y =", slope, "x +", intercept)