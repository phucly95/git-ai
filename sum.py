#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Math utilities module.

This module provides basic mathematical operations.

Author: Your Name
Date: 2024
Version: 1.0
"""

from typing import Union


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together.
    
    This function takes two numeric values and returns their sum.
    Supports both integers and floating-point numbers.
    
    Args:
        a (Union[int, float]): The first number to add.
        b (Union[int, float]): The second number to add.
    
    Returns:
        Union[int, float]: The sum of a and b.
    
    Raises:
        TypeError: If either argument is not a number.
    
    Examples:
        >>> add_numbers(2, 3)
        5
        >>> add_numbers(2.5, 3.7)
        6.2
        >>> add_numbers(-1, 1)
        0
    """
    # Validate input types
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")
    
    # Perform addition and return result
    return a + b