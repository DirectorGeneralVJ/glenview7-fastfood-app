import copy

# ---------------- DATA ----------------
store_data = {
    "GlenView 7": {}
}


# ---------------- CUSTOMER ----------------
class CustomerScreen:
    def __init__(self):
        self.cart = {}
        self.store = None

    def view_stores(self):
        print("\n📍 Stores in Glen View 7")
        if not store_data["GlenView 7"]:
            print("🛑 No stores available.")
            return

        for idx, (name, info) in enumerate(store_data["GlenView 7"].items(), start=1):
            rating = (
                round(sum(info["rating"]) / len(info["rating"]), 2)
                if info["rating"] else "No ratings"
            )
            print(f"{idx}. {name} | {info['location']} | ⭐ {rating}")

    def choose_store(self, index):
        stores = list(store_data["GlenView 7"].keys())
        if 1 <= index <= len(stores):
            self.store = store_data["GlenView 7"][stores[index - 1]]
            self.view_menu()
        else:
            print("❌ Invalid store number.")

    def view_menu(self):
        if not self.store["menu"]:
            print("🛑 This store has no items yet.")
            return

        while True:
            print("\n🍔 Menu")
            for item, price in self.store["menu"].items():
                print(f"{item} - ${price:.2f}")

            self.order_food()
            if input("Continue ordering? (yes/back): ").lower() == "back":
                return

    def order_food(self):
        menu_lookup = {k.lower(): k for k in self.store["menu"]}

        while True:
            choice = input("Item name or 'back': ").lower()
            if choice == "back":
                return

            if choice in menu_lookup:
                real_name = menu_lookup[choice]
                self.cart.setdefault(real_name, {
                    "price": self.store["menu"][real_name],
                    "quantity": 0
                })
                self.cart[real_name]["quantity"] += 1
                print(f"✅ {real_name} added.")
                self.show_cart()
                return
            else:
                print("❌ Item not available. Try again.")

    def show_cart(self):
        print("\n🛒 Your Cart")
        total = 0
        for item, info in self.cart.items():
            cost = info["price"] * info["quantity"]
            print(f"{item} x{info['quantity']} = ${cost:.2f}")
            total += cost
        print(f"💰 Total: ${total:.2f}")
        self.checkout()

    def checkout(self):
        while True:
            confirm = input("Confirm order? (1.Yes / 2.No): ")
            if confirm == "1":
                self.store["orders"].append(copy.deepcopy(self.cart))
                self.cart.clear()
                print("🎉 Order placed successfully!")
                return
            elif confirm == "2":
                print("❌ Order cancelled.")
                return
            else:
                print("Invalid choice.")


# ---------------- SELLER ----------------
class SellerScreen:
    def __init__(self, store_name):
        self.store = store_data["GlenView 7"][store_name]

    def view_orders(self):
        if not self.store["orders"]:
            print("🛑 No new orders.")
            return

        for idx, order in enumerate(self.store["orders"], start=1):
            print(f"\nOrder #{idx}")
            for item, info in order.items():
                print(f"{item} x{info['quantity']}")
        self.store["orders"].clear()

    def add_item(self):
        name = input("Item name: ")
        try:
            price = float(input("Price: "))
            self.store["menu"][name] = price
            print("✅ Item added.")
        except ValueError:
            print("❌ Invalid price.")

    def remove_item(self):
        name = input("Item to remove: ")
        if name in self.store["menu"]:
            del self.store["menu"][name]
            print("❌ Item removed.")
        else:
            print("❌ Item not found.")

    def view_ratings(self):
        ratings = self.store["rating"]
        if ratings:
            print(f"⭐ Average rating: {sum(ratings)/len(ratings):.2f}")
        else:
            print("⭐ No ratings yet.")

    def alert_for_new_orders(self):
        print("🚨 New orders!" if self.store["orders"] else "🛑 No new orders.")


# ---------------- APP ----------------
class FastFoodApp:
    def run(self):
        while True:
            print("\n1.Customer  2.Seller  3.Exit")
            choice = input("Choose role: ")

            if choice == "1":
                customer = CustomerScreen()
                while True:
                    customer.view_stores()
                    pick = input("Store number or 0 to logout: ")
                    if pick == "0":
                        break
                    if pick.isdigit():
                        customer.choose_store(int(pick))

            elif choice == "2":
                name = input("Store name: ")
                if name not in store_data["GlenView 7"]:
                    self.register_store(name)
                seller = SellerScreen(name)
                seller.alert_for_new_orders()

                while True:
                    print("\n1.Orders 2.Add 3.Remove 4.Ratings 5.Exit")
                    action = input("> ")
                    if action == "1": seller.view_orders()
                    elif action == "2": seller.add_item()
                    elif action == "3": seller.remove_item()
                    elif action == "4": seller.view_ratings()
                    elif action == "5": break

            elif choice == "3":
                print("👋 Goodbye.")
                break

    def register_store(self, name):
        location = input("Store location: ")
        store_data["GlenView 7"][name] = {
            "menu": {},
            "rating": [],
            "orders": [],
            "location": location
        }
        print("✅ Store registered.")


if __name__ == "__main__":
    FastFoodApp().run()
