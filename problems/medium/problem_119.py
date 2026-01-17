"""
Problem 119: Speed Filter
Error Type: TYPE_ERROR
Difficulty: Medium
"""

def update_speed(current_val, input_val):
    # Intent: Add input to current
    # Bug: input_val assumed int, might be string (common in input())
    return current_val + input_val

curr = 100
inp = "50"
print(update_speed(curr, inp))