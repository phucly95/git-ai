# Hàm chia hai số
# Hàm này thực hiện phép chia giữa hai giá trị số
# Bao gồm kiểm tra để tránh lỗi chia cho số không
# Tham số: a (số bị chia), b (số chia)
# Trả về: Kết quả của a chia cho b dưới dạng số thực
def div(a, b):
    # Kiểm tra nếu số chia bằng không để tránh ZeroDivisionError
    # Phép chia cho không là không xác định về mặt toán học và sẽ gây ra ngoại lệ
    if b == 0:
        raise ValueError("Cannot divide by zero")
    # Trả về kết quả phép chia
    # Python tự động xử lý phép chia số thực để có kết quả chính xác
    return a / b
