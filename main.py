from system.system import System
class Main:
        def main():
            system = System()
        
        
            while True:
                System.clearScreen()
                print("1. Login")
                print("2. SignUp")
                print("3. Exit")
                choice = input("Enter your choice (1 or 2): ")


                if choice =='1':
                    username= input("Enter the Username: ")
                    password= input("Enter the Password: ")
                    user= system.login(username, password)
                    if user:
                        system.menu(user)
                elif choice == '2':
                        username= input("Enter the Username: ")
                        email = input("Enter the Email: ")
                        password = input("Enter the Password: ")
                        role = input("Enter the Role(Admin, Manager, Chef, Customer): ")
                        system.signup(username, email, password, role)
                elif choice == '3':
                        print("Goodbye!")
                        break
                else:
                        print("Invalid Choice. Please try again. ")

        if __name__ == "__main__":
            main()
                
            
    