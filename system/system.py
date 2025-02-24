from typing import Self
from user.user import User
from admin.admin import Admin
from manager.manager import Manager
from chef.chef import Chef
from customer.customer import Customer
import os


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
    
    
        
    #for login 
    def login(self, Username , Password):
        for user in self.users:
            if user.username== Username and user.password== Password:
                user.resetLoginAttempts()
                return user
            else:
                user.incrementLoginAttempts()
                if user.loginAttempts >=3:
                    print("Login attempt exceed")
                    return None
                print(f"Invalid password. Attempt {user.loginAttempts}/3.")
                return self.login(input("Enter the Username: "), input("Enter the Password: "))
        print("User not found.")
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
            self.admin.adminMenu(user)
        elif user.role=="Manager":
            self.manager.managerMenu(user)
        elif user.role=="Chef":
            self.chef.chefMenu(user)
        elif user.role=="Customer":
            self.customer.customerMenu(user)
    


    
    
            
    
    
    
           
    
    
    
    