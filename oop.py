# Making classes with built in methods and attributes

class Person: #Make a person class and create a greet method
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def greet(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old. Nice to meet you! I am {self.height}cm tall and {self.weight}lbs")


john = Person("John", 56, 170, 150)
mike = Person("Mike", 44, 190, 165)
john.greet()
mike.greet()


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print('Insufficient Funds')

    def display_balance(self):
        print(f"Your balance is ${self.balance}.")

marc = BankAccount("Marc", 100)

marc.withdraw(500)
marc.display_balance()


lein = BankAccount("Lein Sarassra", 1000000)

lein.display_balance()


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (2*self.width + 2*self.length)



school_yard = Rectangle(100, 200)

print(school_yard.area())
print(school_yard.perimeter())


class ShoppingCart:
    def __init__(self, shopper):
        self.shopper = shopper
        self.cart = {}
        self.total = 0

    def add_item(self, name, price):
        self.cart[name] = price

    def remove_items(self, name):
        if name in self.cart:
            self.cart.pop(name)
        else:
            print("This item is not in your cart.")

    def get_total(self):
        total = sum(self.cart.values())
        print(f"Your total is ${total}")

    
    def display_cart(self):
        print(self.cart)


marc = ShoppingCart("Marc")

marc.add_item("Banana", 5)
marc.add_item("Chicken", 8)
marc.add_item("Eggs", 10)
marc.add_item("Butter", 5)
marc.display_cart()
marc.get_total()