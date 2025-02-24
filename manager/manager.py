class Manager:
    def __init__(self, system):
        self.system = system
    
    def managerMenu(self, user):
        print("Manager Menu:")
        print("1. Manage Customers")
        print("2. Manager Menu Categories and Pricing")
        print("3. View Ingredients list Requested by Chefs")
        print("4. Update Profile")
        
        choice = input("Enter your Choice: ")
        
        if choice == '1':
            self.manageCustomers()
        elif choice == '2':
            self.managerMenuCategoriesAndPricing()
        elif choice == '3':
            self.viewIngredientsListRequestedByChefs()
        elif choice == '4':
            self.updateProfile()
        else:
            print("Invalid Choice. Please try again. ")
            
    def manageCustomers(self):
        print("Manage Customers:")
    
    def managerMenuCategoriesAndPricing(self):
        print("Manager Menu Categories and Pricing:")
    
    def viewIngredientsListRequestedByChefs(self):
        print("View Ingredients list Requested by Chefs:")
    
    def updateProfile(self):
        print("Update Profile:")