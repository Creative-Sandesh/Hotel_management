from .admin_menu import manageStaff as manage_staff
from .admin_menu import viewSalesReport as sales_report
from .admin_menu import viewCustomerFeedback as customer_feedback
from .admin_menu import updateProfile as update_profile

class Admin:
    def __init__(self, system):
        self.system = system
        
    def admin_menu(self, user):
        print("Admin Menu:")
        print("1. Manage Staff")
        print("2. View Sales Report")
        print("3. View Customer Feedback")
        print("4. Update Profile")
        choice = input("Enter your Choice: ")
        if choice == '1':
            manage_staff.manage_staff()
        elif choice == '2':
            sales_report.view_sales_report()
        elif choice == '3':
            customer_feedback.view_customer_feedback()
        elif choice == '4':
            update_profile.update_profile()
        else:
            print("Invalid Choice. Please try again.")