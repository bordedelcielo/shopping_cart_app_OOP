class CartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

myItem = CartItem('pizza', '$8.00')

theDict = {'pizza': {myItem}}

print(theDict)

del theDict['pizza']

print(theDict)