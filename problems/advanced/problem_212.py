"""
Problem 212: Hospital SearchEngine
Error Type: LOGICAL
Difficulty: Advanced
"""

class HospitalUser:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class SearchEngine:
    def __init__(self):
        self.users = []
        self.logs = []

    def add_user(self, user):
        self.users.append(user)
        # Bug: Trying to access attribute that might not exist or private
        self.log_action(f"Added {user.username}") # user.name is correct, username wrong

    def log_action(self, msg):
        self.logs.append(msg)

sys = SearchEngine()
u = HospitalUser("Alice", "Admin")
sys.add_user(u)