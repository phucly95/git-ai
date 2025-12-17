"""
Module tiện ích toán học. (human edit)
"""


def cong_hai_so(a: float, b: float) -> float:
    """
    Cộng hai số với nhau.
    
    Tham số:
        a: Số thứ nhất
        b: Số thứ hai
    
    Trả về:
        Tổng của a và b
    """
    return a + b # Trả về tổng 2 số human edit


def nhan_hai_so(a: float, b: float) -> float:
    """
    Nhân hai số với nhau.
    
    Tham số:
        a: Số thứ nhất
        b: Số thứ hai
    
    Trả về:
        Tích của a và b
    """
    return a * b # Trả về tích 2 số human edit


def chia_hai_so(a: float, b: float) -> float:
    """
    Chia số thứ nhất cho số thứ hai.
    
    Tham số:
        a: Số bị chia
        b: Số chia (không được bằng 0)
    
    Trả về:
        Kết quả của phép chia a cho b
    """
    if b == 0:
        raise ValueError("Số chia không được bằng 0.") # Kiểm tra chia cho 0 human edit
    return a / b # Trả về kết quả phép chia human edit


def tru_hai_so(a: float, b: float) -> float:
    """
    Trừ số thứ hai khỏi số thứ nhất.
    
    Tham số:
        a: Số bị trừ
        b: Số trừ
    
    Trả về:
        Hiệu của a và b
    """
    return a - b # Trả về hiệu 2 số human edit