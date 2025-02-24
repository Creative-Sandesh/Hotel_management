import os
def get_sales_data():
    try:
        sales_data = []
        with open("admin\database\sales_data.txt", "r") as file:
            for line in file:
                date, total_sales = line.strip().split(",")
                sales_data.append({"date": date, "total_sales": total_sales})
        return sales_data
    except Exception as e:
        print(f"Error fetching sales data: {e}")
        return []

def view_sales_report():
    try:
        os.system("cls")
        sales_data = get_sales_data()
        if not sales_data:
            print("No sales data available.")
            return
        
        print("Sales Report:")
        for record in sales_data:
            print(f"Date: {record['date']}, Total Sales: ${record['total_sales']}")
        print("End of Sales Report")
    except Exception as e:
        print(f"Error generating sales report: {e}")

if __name__ == "__main__":
    view_sales_report()
    input("Press Enter to continue...")