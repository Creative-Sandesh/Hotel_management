class User:
    def __init__(self, username, email, password, role):
        self.username =username
        self.email = email
        self.password = password
        self.role = role
        self.loginAttempts =0
        
    def resetLoginAttempts(self):
        self.loginAttempts = 0
        
    def incrementLoginAttempts(self):
        self.loginAttempts += 1
        