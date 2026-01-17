"""
Problem 83: Distance Sorter
Error Type: INDEX_ERROR
Difficulty: Medium
"""

def process_distance_data(data):
    # Intent: Process Distance list
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
print(process_distance_data(values))