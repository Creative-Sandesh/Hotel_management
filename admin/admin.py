# admin_menu/updateProfile.py
from system import System

def update_profile():
    username = input("Enter the username of the user you want to update: ")
    system = System()  # Create an instance of the System class to access the data

    # Check if the user is a staff member or customer
    user_found = False
    user = None

    # Check in staff data
    for staff_member in system.users:
        if staff_member.username == username:
            user = staff_member
            user_found = True
            break

    # Check in customer data
    if not user_found:
        for customer in system.customers:
            if customer.username == username:
                user = customer
                user_found = True
                break

    if user_found:
        # Show the current details
        print(f"Current details: Username: {user.username}, Email: {user.email}, Role: {user.role if hasattr(user, 'role') else 'Customer'}")

        # Ask what to update
        print("What would you like to update?")
        option = input("1. Username\n2. Email\n3. Password\n4. Role (only for staff)\nEnter choice (1-4): ")

        if option == '1':
            new_username = input("Enter new username: ")
            user.username = new_username
        elif option == '2':
            new_email = input("Enter new email: ")
            user.email = new_email
        elif option == '3':
            new_password = input("Enter new password: ")
            user.password = new_password
        elif option == '4' and hasattr(user, 'role'):  # Only update role if the user is staff
            new_role = input("Enter new role (e.g., Manager, Chef): ")
            user.role = new_role
        else:
            print("Invalid option.")
            return

        # Save the updated data back to file
        if hasattr(user, 'role'):  # It's a staff member
            system.save_staff_to_file()  # Save updated staff data
        else:  # It's a customer
            system.save_customers_to_file()  # Save updated customer data

        print(f"{username}'s profile has been updated successfully!")
    else:
        print(f"No user found with the username '{username}'.")

    input("Press Enter to continue...")