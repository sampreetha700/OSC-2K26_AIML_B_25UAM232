"""
Problem 246: Gym ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""

class GymReport:
    def __init__(self, data):
        self.data = data
        
    def generate(self):
        report = "REPORT
"
        # Bug: integer iteration over list items directly?
        for i in len(self.data): # TypeError: 'int' object is not iterable
            report += str(self.data[i])
        return report

r = GymReport([1, 2, 3])
print(r.generate())