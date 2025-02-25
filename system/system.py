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
    def clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self):
        self.users = []  
        self.customers = []  
        self.load_staff_from_file()
        self.load_customers_from_file()
        self.admin = Admin(self)
        self.manager = Manager(self)
        self.chef = Chef(self)
        self.customer = Customer(self)

    # Save staff credentials to data.txt
    def save_staff_to_file(self):
        with open('data.txt', 'w') as file:
            for user in self.users:
                if user.role in ["Admin", "Manager", "Chef"]:  
                    file.write(f"{user.username},{user.email},{user.password},{user.role}\n")

    # Save customer credentials to customer_data.txt
    def save_customers_to_file(self):
        with open('Users_database/customer_data.txt', 'w') as file:
            for user in self.customers:  
                file.write(f"{user.username},{user.email},{user.password},{user.role}\n")

    # Load staff credentials
    def load_staff_from_file(self):
        try:
            with open('data.txt', 'r') as file:
                data = file.readlines()
                for line in data:
                    username, email, password, role = line.strip().split(',')
                    user = User(username, email, password, role)
                    self.users.append(user)
        except FileNotFoundError:
            pass

    # Load customer credentials
    def load_customers_from_file(self):
        try:
            with open('Users_database/customer_data.txt', 'r') as file:
                data = file.readlines()
                for line in data:
                    username, email, password, role = line.strip().split(',')
                    user = User(username, email, password, role)
                    self.customers.append(user)
        except FileNotFoundError:
            pass

    # Add a new staff member
    def add_user(self, username, email, password, role):
        user = User(username, email, password, role)
        self.users.append(user)
        self.save_staff_to_file()  

    # Add a new customer
    def add_customer(self, username, email, password):
        user = User(username, email, password, "Customer")
        self.customers.append(user)
        self.save_customers_to_file()  

    # Login method for both staff and customers
    def login(self, username, password):
        for user in self.users + self.customers:  
            if user.username == username and user.password == password:
                user.resetLoginAttempts()
                return user
        
        print("Invalid credentials or user not found!")
        return None

    # Signup method (only for customers)
    def signup(self, username, email, password):
        for user in self.customers:  
            if user.username == username:
                print("Username already exists.")
                return
        self.add_customer(username, email, password)
        print("Customer signed up successfully!")

    # Navigate to the respective menu
    def menu(self, user):
        if user.role == "Admin":
            self.admin.adminMenu(user)
        elif user.role == "Manager":
            self.manager.managerMenu(user)
        elif user.role == "Chef":
            self.chef.chefMenu(user)
        elif user.role == "Customer":
            self.customer.customerMenu(user)
        else:
            print("Role not recognized. Redirecting to home.")
