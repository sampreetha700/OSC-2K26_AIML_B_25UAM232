"""
Problem 85: Distance Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_distance(val):
    # Intent: Check Status
    # Bug: assignment in if
    # if val = 1: # Syntax technically but often passed as logic in detailed description
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    # If val is 20, returns High. If order swapped?
    # if val > 5: return Medium; if val > 10: return High. 20 -> Medium.
    
print(check_distance(20))