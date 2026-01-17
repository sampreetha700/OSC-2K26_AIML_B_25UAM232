"""
Problem 282: Email ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""

class EmailReport:
    def __init__(self, data):
        self.data = data
        
    def generate(self):
        report = "REPORT
"
        # Bug: integer iteration over list items directly?
        for i in len(self.data): # TypeError: 'int' object is not iterable
            report += str(self.data[i])
        return report

r = EmailReport([1, 2, 3])
print(r.generate())