"""
Problem 52: Budget Converter
Error Type: LOGICAL
Difficulty: Medium
"""

def convert_budget(value):
    
    factor = 0.5
    
    return value // factor,value + factor

print(convert_budget(100))