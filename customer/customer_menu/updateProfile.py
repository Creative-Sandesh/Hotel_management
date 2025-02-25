CUSTOMER_FILE = "Users_database/customer_data.txt"

def update_profile(username):
    """Allows customers to update their profile details."""
    
    # Read customer data
    customers = []
    found = False

    try:
        with open(CUSTOMER_FILE, "r") as file:
            customers = file.readlines()
    except FileNotFoundError:
        print("Customer data not found.")
        return

    # Find and update user
    for i, line in enumerate(customers):
        details = line.strip().split(",")
        if details[0] == username:
            found = True
            print(f"\nCurrent Profile:\nUsername: {details[0]}\nEmail: {details[1]}\nPassword: {details[2]}")
            choice = input("What do you want to update? (1: Email, 2: Password): ")

            if choice == '1':
                details[1] = input("Enter new email: ").strip()
            elif choice == '2':
                details[2] = input("Enter new Password number: ").strip()
            else:
                print("Invalid choice. No updates made.")
                return

            customers[i] = ",".join(details) + "\n"
            break

    if found:
        try:
            with open(CUSTOMER_FILE, "w") as file:
                file.writelines(customers)
            print("Profile updated successfully!")
        except Exception as e:
            print(f"Error updating profile: {e}")
    else:
        print("User not found.")
