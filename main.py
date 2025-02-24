from system.system import System
class Main:
        def main():
            system = System()
        
        
            while True:
                print("Welcome! Please choose an option:")
                print("1. Staff Login (Admin, Manager, Chef)")
                print("2. Non-Staff Login (Customer)")
                print("3. Sign Up as Customer")
                print("4. Exit")
                
                choice = input("Enter your choice: ")
                
                if choice == '1':
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    user = system.login(username, password)
                    if user:
                        print(f"Welcome {user.username}! ({user.role})")
                        system.menu(user)
                    else:
                        print("Invalid username or password. Please try again.")
                elif choice == '2':
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    #Chech if the user is a customer
                    user = system.login(username, password)
                    
                    if user and user.role=="Customer":
                        print(f"Welcome {user.username}! ({user.role})")
                        system.menu(user)
                    else:
                        print("Invalid username or password. Please try again.")
                
                elif choice == '3': 
                    username = input("Enter your username: ")
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    role = "Customer"
                    system.signup(username,email,password,role)
                
                elif choice == '4':
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
                                  
                
        if __name__ == "__main__":
            main()
                
            
    