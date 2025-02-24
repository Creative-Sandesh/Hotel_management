class Chef:
    def __init__(self,system):
        self.system = system
    
    def chefMenu(self,user):
        print("Chef Menu:")
        print("1. View Orders")
        print("2. Update Orders")
        print("3. Request Ingredients")
        print("4. Update Profile")
        choice = input("Enter Your Choice: ")
        if choice == '1':
            self.viewOrders()
        elif choice == '2':
            self.updateOrders()
        elif choice == '3':
            self.requestIngredients()
        elif choice == '4':
            self.updateProfile()
        else:
            print("Invalid Choice. Please try again. ")
            
    def viewOrders(self):
        print("View Orders:")
    
    def updateOrders(self):
        print("Update Orders:")
    
    def requestIngredients(self):
        print("Request Ingredients:")
    
    def updateProfile(self):
        print("Update Profile:")