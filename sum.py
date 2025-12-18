"""
Mathematical utility module. (human edit)
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
    return a + b  # Return the sum of 2 numbers


def multiply_two_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b  # Return the product of 2 numbers


def divide_two_numbers(a: float, b: float) -> float:
    """
    Divide the first number by the second number.
    
    Args:
        a: Dividend
        b: Divisor (cannot be 0)
    
    Returns:
        Result of dividing a by b
    """
    if b == 0:
        raise ValueError("Divisor cannot be zero.")  # Check for division by zero
    return a / b  # Return the division result


def subtract_two_numbers(a: float, b: float) -> float:
    """
    Subtract the second number from the first number.
    
    Args:
        a: Minuend
        b: Subtrahend
    
    Returns:
        Difference of a and b
    """
    return a - b  # Return the difference of 2 numbers (human edit)

# (human edit)