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
        self.shopping_cart = []

    # def delete_item(self):
    #     removed_item = input('What is the name of the item you would like to remove?: ').title()
    #     self.shopping_cart.remove(removed_item)

    # def __str__(self):
    #     return self.shopping_cart


    def format_items(self):
        for item in self.shopping_cart:
            print(item)
            print("=" * 60)

    def delete_items(self):
        item_to_delete = input("What's the name of the item you'd like to add?: ").title()
        self.shopping_cart.remove(item_to_delete)

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
                name = input("What's the name of the item you'd like to add?: ").title()
                price = random.randint(1,10)
                item = CartItem(name, price)
                self.shopping_cart.append(item)
            elif decision == "remove":
                self.delete_items()
            elif decision == "review":
                self.format_items()
            elif decision == "help":
                print(
                    "This application is a shopping cart. You add whatever you wish into it, take items out, and take a"
                    " look at your current shopping cart list. Thanks for using our software!")

    def run_program(self):
        self.run()


shopping_cart = ShoppingCart()
shopping_cart.run_program()

# first = ["eggs", "bacon"]
#
# for i in first:
#     print(repr(i))


