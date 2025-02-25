import os

def update_profile():
    try:
        print("Update Profile:")
        # Example profile data
        profile = {
            "username": "admin",
            "email": "admin@example.com",
            "password": "123-456-7890"
        }
        
        print(f"Current Profile:\nUsername: {profile['username']}\nEmail: {profile['email']}\nPassword: {profile['phone']}")
        
        choice = input("What do you want to update? (1: Username, 2: Email, 3: Password): ")
        
        if choice == '1':
            profile['username'] = input("Enter new username: ")
        elif choice == '2':
            profile['email'] = input("Enter new email: ")
        elif choice == '3':
            profile['password'] = input("Enter new Password: ")
        else:
            print("Invalid choice. No updates made.")
        
        # Save the updated profile (Here, we're just printing it for simplicity)
        print(f"Updated Profile:\nUsername: {profile['username']}\nEmail: {profile['email']}\nPassword: {profile['password']}")
    
    except Exception as e:
        print(f"Error updating profile: {e}")

if __name__ == "__main__":
    os.system("cls")
    update_profile()
    