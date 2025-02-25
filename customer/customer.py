from customer.customer_menu import viewAndOrderFood
from customer.customer_menu import viewOrderStatus
from customer.customer_menu import sendFeedback
from customer.customer_menu import updateProfile

class Customer:
    def __init__(self, system):
        self.system = system

    def customerMenu(self, user):
        """Displays the customer menu and handles choices."""
        while True:
            print("\n--- Customer Menu ---")
            print("1. View & Order Food")
            print("2. View Order Status")
            print("3. Send Feedback")
            print("4. Update Profile")
            print("5. Exit")
            
            choice = input("Enter your Choice: ")
            
            if choice == '1':
                viewAndOrderFood.view_and_order_food(user.username)
            elif choice == '2':
                viewOrderStatus.view_order_status(user.username)
            elif choice == '3':
                sendFeedback.send_feedback(user.username)
            elif choice == '4':
                updateProfile.update_profile(user.username)
            elif choice == '5':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid Choice. Please try again.")
