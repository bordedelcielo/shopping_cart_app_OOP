import random
from random import seed
from random import randint


class CartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item: {self.name} ||| Cost: ${self.price}"


class ShoppingCart:
    def __init__(self):
        self.shopping_cart = {}

    def format_items(self):
        for item in list(self.shopping_cart.values()):
            print(item)
            print("=" * 60)

    def print_cart(self):
        print(self.shopping_cart)

    def add_items(self):
        item_to_add = input('What\'s the name of the item you\'d like to add?: ').title()
        price = random.randint(1,10)
        item_object = CartItem(item_to_add, price)
        self.shopping_cart[item_to_add] = item_object

    def delete_items(self):
        item_to_delete = input("What's the name of the item you'd like to delete?: ").title()
        del self.shopping_cart[item_to_delete]

    def run(self):
        done = False

        while not done:
            decision = input(
                "\nWelcome to your shopping cart! Would you like to add items to cart, \nremove them, review your "
                "cart, "
                "need help, or done? (Add, Remove, Review, Help, or Done): ").lower()

            if decision == 'done':
                print("\nGoodbye! Thanks for shopping!")
                done = True
            elif decision == 'add':
                self.add_items()
            elif decision == "remove":
                self.delete_items()
            elif decision == "review":
                self.format_items()
            elif decision == "print":
                self.print_cart()
            elif decision == "help":
                print(
                    "This application is a shopping cart. You add whatever you wish into it, take items out, and take a"
                    " look at your current shopping cart list. Thanks for using our software!")


my_cart = ShoppingCart()
my_cart.run()