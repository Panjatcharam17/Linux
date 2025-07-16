class Order:
    def __init__(self, customer_name, item, item_amount, discount):
        self.customer_name = customer_name      # Public
        self.item = item                        # Public
        self.__item_amount = item_amount        # Private
        self.__discount = discount              # Private
        self.__total_amount = item_amount       # Internal total amount before discount

    def __calculate_final(self):                # Private helper method
        return self.__total_amount - self.__discount

    def _get_admin_view(self):                  # Protected method
        return {
            "Customer": self.customer_name,
            "Items": self.item,
            "Total Amount": f"{self.__total_amount}",
            "Discount Applied": f"{self.__discount}",
            "Final Bill": f"{self.__calculate_final()}"
        }

    def get_customer_view(self):                # Public method
        return {
            "Customer": self.customer_name,
            "Items": self.item,
            "Final Bill": f"{self.__calculate_final()}"
        }

class AdminPortal:
    def show_order(self, order):
        return order._get_admin_view()          # Allowed (protected access)

class CustomerApp:
    def show_order(self, order):
        return order.get_customer_view()        # Safe (public access)

# Test the setup
order = Order("Panjatcharam", ["Pizza", "Pepsi"], 600, 100)

admin = AdminPortal()
customer = CustomerApp()

print("✅ Admin View:")
print(admin.show_order(order))

print("\n👤 Customer View:")
print(customer.show_order(order))



"""
OUTPUT:
✅ Admin View:
{'Customer': 'Panjatcharam', 'Items': ['Pizza', 'Pepsi'], 'Total Amount': '600', 'Discount Applied': '100', 'Final Bill': '500'}

👤 Customer View:
{'Customer': 'Panjatcharam', 'Items': ['Pizza', 'Pepsi'], 'Final Bill': '500'}
"""