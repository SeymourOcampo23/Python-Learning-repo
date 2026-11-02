def show(a, b, c=0, d=0):
    print(a, b, c, d)


args = [1, 2]
options = {"d": 9, "c": 2} #dict keys must match parameter names 

show(*args, **options)

def dog(breed="", sex="", size=0): #example 
    print(f"My dog is a {breed}, he is a {sex}, and is {size} meter tall")

beagle = {"breed": "beagle", "sex": "male", "size": 1}

dog(**beagle)

# Exercises
# Write multiply(a, b). Call it with a list [4, 5] using *.

def multiply(a, b):
    return (a * b)
nums = [4, 5]

print(multiply(*nums))



# Write greet(first, last). Call it with a dictionary using **.

def greet(first, last):
    return f"Hi, {first} {last}"

name = {"first": "Seymour", "last": "Ocampo"}

print(greet(**name))

# Make two dictionaries, defaults and overrides. Merge them into one new 
# dictionary using **. Print the result.

defaults = {"temp": 90, "speed": 120, "altitude": 1000}
overrides = {"depth": -20000, "acceleration": 99, "temp": 120}

merged = {**defaults, **overrides} #the later "temp" value will be printed because it 
# is added later
print(merged)

merged = {**overrides, **defaults} #I switched the order of the dictionaries 
# and so did the value of temp
print(merged)

def start_chat(user, history=[]):
    history.append(f"Hello {user}!")
    return history

alice_chat = start_chat("Alice")
bob_chat = start_chat("Bob")

print(alice_chat)  # ['Hello Alice!', 'Hello Bob!']
print(bob_chat) # ['Hello Alice!', 'Hello Bob!']


# using none, only one item is added to items
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

my_list = ["x"]

print(add_item("y", my_list))


def add_to_cart(item, cart=None, **options):
    if cart is None:
        cart = []
    cart.append({"item": item, **options})
    return cart

details = {"qty": 2, "color": "red"}
print(add_to_cart("shirt", **details))

print(add_to_cart("book", qty=5)) #Uses different carts
print(add_to_cart("Watch", qty=1))

names = ["hat", "socks", "belt"]

print(*names, sep=", ")





    











