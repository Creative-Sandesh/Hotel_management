from system.system import System  

def main():
    system = System()
    
    print("Are you staff or a customer?")
    user_type = input("Enter 'staff' or 'customer': ").strip().lower()

    if user_type == "staff":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = system.login(username, password)
        if user and user.role in ["Admin", "Manager", "Chef"]:
            print(f"Welcome {user.username}! Role: {user.role}")
            system.menu(user)
        else:
            print("Invalid credentials or you are not staff!")

    elif user_type == "customer":
        print("1. Login")
        print("2. Sign Up")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = system.login(username, password)
            if user and user.role == "Customer":
                print(f"Welcome {user.username}!")
                system.menu(user)
            else:
                print("Invalid credentials!")

        elif choice == "2":
            username = input("Enter a username: ")
            email = input("Enter your email: ")
            password = input("Enter a password: ")
            system.signup(username, email, password)
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
