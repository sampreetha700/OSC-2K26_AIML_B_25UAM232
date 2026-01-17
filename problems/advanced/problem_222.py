"""
Problem 222: School ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""

class SchoolReport:
    def __init__(self, data):
        self.data = data
        
    def generate(self):
        report = "REPORT
"
        # Bug: integer iteration over list items directly?
        for i in len(self.data): # TypeError: 'int' object is not iterable
            report += str(self.data[i])
        return report

r = SchoolReport([1, 2, 3])
print(r.generate())