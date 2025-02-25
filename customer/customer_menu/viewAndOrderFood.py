FOOD_MENU_FILE = "Users_database/food_menu.txt"
ORDER_FILE = "Users_database/customer_orders.txt"

def view_and_order_food(username):
    """Displays the food menu and allows the customer to place an order."""
    
    # Read the food menu
    menu = {}
    try:
        with open(FOOD_MENU_FILE, "r") as file:
            print("\n--- Food Menu ---")
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    food_item, price = parts
                    menu[food_item] = float(price)
                    print(f"{food_item} - Rs. {price}")
    except FileNotFoundError:
        print("Sorry, the food menu is currently unavailable.")
        return

    # Taking customer order
    order = {}
    while True:
        item = input("\nEnter the food item to order (or type 'done' to finish): ").strip()
        if item.lower() == "done":
            break
        if item not in menu:
            print("Invalid item. Please choose from the menu.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {item}: "))
            if quantity > 0:
                order[item] = quantity
            else:
                print("Quantity must be at least 1.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")

    if not order:
        print("No items ordered.")
        return

    # Calculate total cost
    total_cost = sum(menu[item] * qty for item, qty in order.items())
    
    # Save order details
    try:
        with open(ORDER_FILE, "a") as file:
            file.write(f"{username},{order},{total_cost}\n")
        print("\nOrder placed successfully!")
        print(f"Total amount: Rs. {total_cost}")
    except Exception as e:
        print(f"Error saving order: {e}")
        

    # Display order details
    print("\n--- Order Details ---")
    for item, qty in order.items():
        print(f"{item} - Quantity: {qty}")
    print(f"Total Cost: Rs. {total_cost}")

    print("\nReturning to Main Menu...")

    return

