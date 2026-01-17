"""
Problem 280: Email DatabaseManager
Error Type: LOGICAL
Difficulty: Advanced
"""

class EmailRecord:
    def __init__(self, id, data):
        self.id = id
        self.data = data

class DatabaseManager:
    def __init__(self):
        self.db = {}
        
    def save(self, record):
        # Bug: Using record as key directly (unhashable check?)
        # Or overwriting incorrectly
        self.db[record.id] = record
        
    def get(self, id):
        return self.db.get(id) # returns None if missing
        
    def update(self, id, new_data):
        rec = self.get(id)
        # Bug: what if rec is None?
        rec.data = new_data # AttributeError if None
        
m = DatabaseManager()
m.update(99, "New") # 99 doesn't exist