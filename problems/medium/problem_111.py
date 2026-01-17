"""
Problem 111: Steps Sorter
Error Type: INDEX_ERROR
Difficulty: Medium
"""

def process_steps_data(data):
    # Intent: Process Steps list
    results = []
    # Bug: range goes one past the end
    for i in range(len(data) + 1):
        if i < len(data):
             results.append(data[i] * 2)
        else:
             # This block shouldn't be reached if logic was correct but loop is wrong
             results.append(data[i]) # Boom
    return results

values = [10, 20, 30]
print(process_steps_data(values))