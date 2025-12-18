# Hàm chia hai số
def div(a, b):
    # Kiểm tra nếu số chia bằng 0
    if b == 0:
        raise ValueError("Cannot divide by zero")
    # Trả về kết quả phép chia
    return a / b
