"""
Problem 258: Traffic ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""

class TrafficReport:
    def __init__(self, data):
        self.data = data
        
    def generate(self):
        report = "REPORT
"
        # Bug: integer iteration over list items directly?
        for i in len(self.data): # TypeError: 'int' object is not iterable
            report += str(self.data[i])
        return report

r = TrafficReport([1, 2, 3])
print(r.generate())