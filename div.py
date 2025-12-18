# Divide two numbers
def div(a, b):
    # Check for division by zero
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
