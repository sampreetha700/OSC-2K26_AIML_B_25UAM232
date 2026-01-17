"""
Problem 66: Temperature Converter
Error Type: LOGICAL
Difficulty: Medium
"""

def convert_temperature(value):
    # Intent: Convert units
    factor = 0.5
    # Bug: Integer division or wrong formula
    return value // factor # Returns 0.0 if value < factor? No, 10 // 0.5 is 20.0
    # Let's say: value + factor instead of *
    return value + factor

print(convert_temperature(100))