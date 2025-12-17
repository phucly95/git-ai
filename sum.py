"""
Math utilities module. (human edit)
"""


def add_two_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b  # Return sum of 2 numbers


def multiply_two_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b  # Return product of 2 numbers


def divide_two_numbers(a: float, b: float) -> float:
    """
    Divide first number by second number.
    
    Args:
        a: Dividend
        b: Divisor (cannot be zero)
    
    Returns:
        Result of dividing a by b
    """
    if b == 0:
        raise ValueError("Divisor cannot be zero.")  # Check division by zero
    return a / b  # Return division result


def subtract_two_numbers(a: float, b: float) -> float:
    """
    Subtract second number from first number.
    
    Args:
        a: Minuend
        b: Subtrahend
    
    Returns:
        Difference of a and b
    """
    return a - b  # Return difference of 2 numbers


# human edit