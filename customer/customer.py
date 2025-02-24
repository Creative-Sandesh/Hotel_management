
class Customer:
    def __init__(self, system):
        self.system = system

    def customerMenu(self, user):
        print("Customer Menu:")
        print("1. View & Order Food")
        print("2. View Order Status")
        print("3. Send Feedback")
        print("4. Update Profile")
        choice = input("Enter your Choice: ")
        if choice == '1':
            self.viewAndOrderFood()
        elif choice == '2':
            self.viewOrderStatus()
        elif choice == '3':
            self.sendFeedback()
        elif choice == '4':
            self.updateProfile()
        else:
            print("Invalid Choice. Please try again. ")

    def viewAndOrderFood(self):
        print("View & Order Food:")  
        
    def viewOrderStatus(self):
        print("View Order Status:")
          
    def sendFeedback(self):  
        print("Send Feedback:")
          
    def updateProfile(self):
        print("Update Profile:")