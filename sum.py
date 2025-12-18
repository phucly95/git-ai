"""
Module tiện ích toán học. (human edit)
"""


def add_two_numbers(a: float, b: float) -> float:
    """
    Cộng hai số với nhau.
    
    Args:
        a: Số thứ nhất
        b: Số thứ hai
    
    Returns:
        Tổng của a và b
    """
    return a + b  # Trả về tổng của 2 số


def multiply_two_numbers(a: float, b: float) -> float:
    """
    Nhân hai số với nhau.
    
    Args:
        a: Số thứ nhất
        b: Số thứ hai
    
    Returns:
        Tích của a và b
    """
    return a * b  # Trả về tích của 2 số


def divide_two_numbers(a: float, b: float) -> float:
    """
    Chia số thứ nhất cho số thứ hai.
    
    Args:
        a: Số bị chia
        b: Số chia (không thể bằng 0)
    
    Returns:
        Kết quả của phép chia a cho b
    """
    if b == 0:
        raise ValueError("Số chia không thể bằng 0.")  # Kiểm tra chia cho 0
    return a / b  # Trả về kết quả phép chia


def subtract_two_numbers(a: float, b: float) -> float:
    """
    Trừ số thứ hai khỏi số thứ nhất.
    
    Args:
        a: Số bị trừ
        b: Số trừ
    
    Returns:
        Hiệu của a và b
    """
    return a - b  # Trả về hiệu của 2 số

# human edit
# human edit