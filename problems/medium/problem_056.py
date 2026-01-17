"""
Problem 56: Budget Filter
Error Type: TYPE_ERROR
Difficulty: Medium
"""

def update_budget(current_val, input_val):
    # Intent: Add input to current
    # Bug: input_val assumed int, might be string (common in input())
    return current_val + input_val

curr = 100
inp = "50"
print(update_budget(curr, inp))