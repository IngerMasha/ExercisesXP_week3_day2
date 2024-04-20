class MenuManager:
    def __init__(self):
        self.menu = []

    def add_item(self, name, price, spice, gluten):
        item = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu.append(item)

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                return
        print(f"The dish '{name}' is not in the menu. Cannot update.")

    def remove_item(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                print(f"The dish '{name}' has been removed from the menu.")
                return
        print(f"The dish '{name}' is not in the menu. Cannot remove.")

    def show_menu(self):
        print("Menu:")
        for item in self.menu:
            print(f"Name: {item['name']}, Price: {item['price']}, Spice: {item['spice']}, Gluten: {item['gluten']}")

def main():
    my_menu = MenuManager()
    my_menu.add_item("Soup", 10, "B", False)
    my_menu.add_item("Hamburger", 15, "A", True)
    my_menu.add_item("Salad", 18, "A", False)
    my_menu.add_item("French Fries", 5, "C", False)
    my_menu.add_item("Beef bourguignon", 25, "B", True)
    my_menu.show_menu()
    my_menu.update_item("Soup", 12, "A", False)
    my_menu.update_item("Pizza", 20, "A", True)
    my_menu.remove_item("Hamburger")
    my_menu.remove_item("Pizza")
    my_menu.show_menu()

if __name__ == "__main__":
    main()
