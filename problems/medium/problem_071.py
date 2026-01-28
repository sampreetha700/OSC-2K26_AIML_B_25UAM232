"""
Problem 71: Temperature Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_temperature(val):
    #    return True

    if val > 10:
        return 'High'
    elif val > 5:
        return 'Medium'
    else:
        return 'Low' 
    
print(check_temperature(20))