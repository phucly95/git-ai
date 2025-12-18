# Function to divide two numbers
# This function performs division operation between two numeric values
# It includes validation to prevent division by zero errors
# Parameters: a (dividend), b (divisor)
# Returns: The result of a divided by b as a float
def div(a, b):
    # Check if divisor is zero to avoid ZeroDivisionError
    # Division by zero is mathematically undefined and will raise an exception
    if b == 0:
        raise ValueError("Cannot divide by zero")
    # Return the division result
    # Python automatically handles float division for accurate results
    return a / b
