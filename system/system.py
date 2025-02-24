from admin.admin import Admin
from manager.manager import Manager
from chef.chef import Chef
from customer.customer import Customer
import os


class User:
    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.loginAttempts = 0

    def resetLoginAttempts(self):
        self.loginAttempts = 0

    def incrementLoginAttempts(self):
        self.loginAttempts += 1
        


class System:
    
    
    # clear the screen function
    def clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
    #creating the constructure
    def __init__(self):
        self.users=[] #constructor method initializes an empty list called users to store instances of User
        self.load_users_to_file()
        self.admin = Admin(self)
        self.manager = Manager(self)
        self.chef = Chef(self)
        self.customer = Customer(self)
        
    
        # method for save the signup data
    def save_users_to_file(self):
        with open ('data.txt','w') as file:
            for user in self.users:
                file.write(f"{user.username},{user.email},{user.password},{user.role}\n")
    

    
    #method for load the stored from text file
    def load_users_to_file(self):
        try:
            with open('data.txt','r') as file:
                data=file.readlines()
                for line in data:
                    username, email, password, role = line.strip().split(',')
                    user = User(username,email,password,role)
                    self.users.append(user)
        except FileNotFoundError:
            pass
    
           
        
    #method for adding user data to User class instance
    def add_user(self, username , email, password, role):
        user= User(username,email, password, role)
        self.users.append(user)
        self.save_users_to_file()
    
    
        
    #for login page
    
    def login(self,username,password):
        attempts = 0
        while attempts < 3:
            for user in self.users:
                if user.username== username and user.password==password:
                    user.resetLoginAttempts()
                    return user
            attempts += 1
            print(f"Invalid password. Attempt {attempts}/3.")
            if attempts < 3:
                username = input("Enter the Username: ")
                password = input("Enter the Password: ")
        print("Login attempt exceed")
        return None
    
    # sign Up page
    def signup(self, username ,email, password,role):
        for user in self.users:
            if user.username== username:
                print("Username already exists.")
                return
        self.add_user(username, email, password,role)
        print("User signed up successfully!")
        
        
    #for Menu page
    def menu(self, user):
        if user.role == "Admin":
            self.admin.admin_menu(user)
        elif user.role=="Manager":
            self.manager.managerMenu(user)
        elif user.role=="Chef":
            self.chef.chefMenu(user)
        elif user.role=="Customer":
            self.customer.customerMenu(user)
        else:
            print("Role not recognized. Redirecting to home.")
    


    
    
            
    
    
    
           
    
    
    
    