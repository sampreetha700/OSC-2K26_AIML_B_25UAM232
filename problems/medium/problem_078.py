"""
Problem 78: Currency Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_currency(val):
    #    return True

    if val > 10:
        return 'High'
    elif val > 5:
        return 'Medium'
    else:
        return 'Low' 
    
print(check_currency(20))