class Cart:

    def __init__(self):
        self.items = {}
        self.price_details = {"books": 200, "pens": 10, "notebooks": 50, "erasers": 5}

    def add_item(self, item, quantity):
        if item in self.price_details:
            self.items[item] = self.items.get(item, 0) + quantity
            print(item, "added successfully.")
        else:
            print("Product not available.")

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(item, "removed.")
        else:
            print("Item not found.")

    def update_quantity(self, item, quantity):
        if item in self.items:
            self.items[item] = quantity
            print("Quantity updated.")
        else:
            print("Item not found.")

    def view_cart(self):
        if len(self.items) == 0:
            print("\nCart is Empty")
        else:
            print("\nYour Cart")
            for item, qty in self.items.items():
                print(item, ":", qty)

    def total_price(self):
        total = 0
        for item, qty in self.items.items():
            total += qty * self.price_details[item]
        print("Total Price = ₹", total)


cart = Cart()

while True:

    print("\n========== SHOPPING CART ==========")
    print("1. Add Item")
  
    print("3. Update Quantity")
    print("4. View Cart")
    print("5. Total Price")
    print("6. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        print("\nAvailable Products:")
        for item, price in cart.price_details.items():
            print(item, "-", price)

        item = input("Enter Item : ").lower()
        qty = int(input("Enter Quantity : "))
        cart.add_item(item, qty)
    elif choice == 2:
        item = input("Enter Item : ").lower()
        cart.remove_item(item)
    
    elif choice == 3:
        item = input("Enter Item : ").lower()
        qty = int(input("Enter New Quantity : "))
        cart.update_quantity(item, qty)

    elif choice == 4:
        cart.view_cart()

    elif choice == 5:
        cart.total_price()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")