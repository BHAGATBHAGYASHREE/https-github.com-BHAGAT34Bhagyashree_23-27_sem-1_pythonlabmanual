class Store:
    def __init__(self):
        self.products = {
            '001': {'name': 'Product1', 'price': 10.0},
            '002': {'name': 'Product2', 'price': 15.0},
            '003': {'name': 'Product3', 'price': 20.0},
        }
        self.cart = {}

    def display_menu(self):
        print("Product Code | Product Name | Price")
        print("-----------------------------------")
        for code, info in self.products.items():
            print(f"{code} | {info['name']} | ${info['price']:.2f}")

    def take_order(self):
        while True:
            code = input("Enter the product code (or 'done' to finish): ")
            if code.lower() == 'done':
                break

            if code in self.products:
                quantity = int(input(f"Enter the quantity for {self.products[code]['name']}: "))
                if code in self.cart:
                    self.cart[code]['quantity'] += quantity
                else:
                    self.cart[code] = {'name': self.products[code]['name'], 'price': self.products[code]['price'], 'quantity': quantity}
            else:
                print("Invalid product code. Please enter a valid code.")

    def generate_bill(self):
        total_amount = 0.0
        print("\n\n========== Bill ==========")
        print("Product | Quantity | Price | Total")
        print("---------------------------------")
        for code, item in self.cart.items():
            total_item_price = item['price'] * item['quantity']
            total_amount += total_item_price
            print(f"{item['name']} | {item['quantity']} | ${item['price']:.2f} | ${total_item_price:.2f}")

        print("---------------------------------")
        print(f"Total Amount: ${total_amount:.2f}")

    def run(self):
        print("Welcome to the Store!")
        self.display_menu()
        self.take_order()
        self.generate_bill()


if __name__ == "__main__":
    my_store = Store()
    my_store.run()
