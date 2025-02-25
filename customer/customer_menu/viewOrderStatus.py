ORDER_FILE = "Users_database/customer_orders.txt"

def view_order_status(username):
    """Displays the status of the customer's past orders."""
    
    try:
        with open(ORDER_FILE, "r") as file:
            orders = file.readlines()
        
        print("\n--- Your Order History ---")
        found = False
        for order in orders:
            details = order.strip().split(",")
            if details[0] == username:
                print(f"Order: {details[1]} | Total Cost: Rs. {details[2]}")
                found = True
        
        if not found:
            print("No orders found.")
    except FileNotFoundError:
        print("No order history available.")
        