# Function to divide two numbers
def div(a, b):
    # Check if divisor is zero
    if b == 0:
        raise ValueError("Cannot divide by zero")
    # Return the division result
    return a / b
