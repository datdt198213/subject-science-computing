def lagrange_line(x, x1, y1, x2, y2):
    # Tính giá trị đa thức Lagrange cho đường thẳng
    y = ((x - x2) / (x1 - x2)) * y1 + ((x - x1) / (x2 - x1)) * y2
    return y

# Gọi hàm để tính giá trị đường thẳng tại một điểm x
x = 4
x1 = 1
y1 = 2
x2 = 5
y2 = 7

result = lagrange_line(x, x1, y1, x2, y2)
print(f"Giá trị của đường thẳng tại điểm x = {x} là {result}")

# Thay giá trị tại điểm x = 4 vào các phương trình trong đáp án
# Nếu thấy bằng với result thì chọn
# Trong trường hợp có 2 kết quả thì thay đổi x là một giá trị khác và thử lại
