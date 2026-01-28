"""
Problem 57: Budget Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_budget(val):
    

    if val > 10:
        return 'High'
    elif val > 5:
        return 'Medium'
    else:
        return 'Low' 
    
    
print(check_budget(6))