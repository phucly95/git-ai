# Advanced mathematical division utility for testing purposes
# This utility provides safe division operations with comprehensive error handling
# Designed for testing mathematical calculations in various scenarios
# Input: a (numerator value), b (denominator value)
# Output: Floating point result of the division operation
def div(a, b):
    # Validate denominator to prevent mathematical errors
    # Zero division would cause undefined behavior in mathematical operations
    if b == 0:
        raise ValueError("Cannot divide by zero")
    # Execute division and return precise floating point result
    # Uses Python's built-in division operator for maximum accuracy
    return a / b
