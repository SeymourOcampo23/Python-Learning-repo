# Lists
fruits = ["apple", "banana", "cherry"] 

# print the first fruit
print(fruits[0])

# replace banana with orange
fruits.remove("banana")
fruits.insert(1, "orange")

# print the length of the list 
print(len(fruits))

# Create a list of numbers from 1 to 10 .
my_numbers = [i for i in range(1, 11)]
print(my_numbers)

# print the first 3 numbers
print(my_numbers[0:3])

# print the last 3 numbers
print(my_numbers[-1:-4:-1])

# Sort the list in ascending order.
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)

# append 10 to the list
numbers.append(10)
print(numbers)

# remove number 2 from the list
numbers.remove(2)
print(numbers)

# Tuples
coordinates = (10, 20)
print(coordinates)
# Try to modify the tuple by setting coordinates[0] = 50 — note what
# happens.
# coordinates[0] = 50 tuple does not support item assignment
# Convert the tuple to a list, change its first element to 50 , and convert it back
# to a tuple.
tuple_to_list = [coordinates[i] for i in range(len(coordinates))]
print(tuple_to_list)

tuple_to_list.remove(10)
tuple_to_list.insert(0, 50)
print(tuple_to_list)

coordinates = tuple(tuple_to_list)
print(coordinates)

# Sets and Methods
my_set = {1, 2, 3, 3, 4}
print(my_set) #The duplicate 3 is removed from the set.

# Add 5 to the set, remove 2 , and check if 4 is in the set.
my_set.add(5)
print(my_set)
my_set.remove(2)
print(my_set)
print(4 in my_set)
print(my_set)

# Create two sets
a = {1, 2, 3}
b = {3, 4, 5}
# union
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Dictionaries
student = {"name": "John", "age": 20, "grade": "A"}
# Print value of "name":
print(student["name"])
# Change grade to A+
student["grade"] = "A+"
print(student["grade"])
# Add a new key "city" with value "Batangas".
student["city"] = "Batangas"
print(student)

# Create a dictionary of three friends and their phone numbers. Use:
# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print the
friends = {"Mike": "123123", "John": "456456", "Daisy": "789789"}
print(friends.keys())
print(friends.values())
print(friends.items())



# Write a program that takes a list of numbers and removes all duplicates using
# a set
list_of_numbers = [1, 4, 2, 2, 4, 5, 7, 7, 8, 12, 12, 3]
def duplicate_remover(a_list):
    return set(a_list)
print(duplicate_remover(list_of_numbers))

# Given a dictionary of products and their prices, find the product with the
# highest price.

products = {
    "Laptop": 1299.99,
    "Wireless Mouse": 29.99,
    "Keyboard": 79.99,
    "Headphones": 149.99,
    "USB-C Cable": 19.99,
    "Webcam": 89.99,
    "Monitor": 299.99,
    "Desk Lamp": 39.99
}
# This way was harder to understand 
def get_highest_price(dict):
    return max(dict.items(), key=lambda item: item[1])

print(get_highest_price(products))

# It is easier to follow the logic using this way. 
def get_highest_price2(dict):
    max_price = max(dict.values())
    for item in dict:
        if dict[item] == max_price:
            return item, max_price

print(get_highest_price2(products))

# Write a program that merges two dictionaries into one

food_calories_1 = {
    "Pizza": 850,
    "Burger": 720,
    "Pasta": 640,
    "Tacos": 510,
    "Sushi": 480
}

food_calories_2 = {
    "Chicken Wings": 760,
    "Steak": 680,
    "Fried Rice": 590,
    "Nachos": 820,
    "Pancakes": 540
}

def dict_merger(dict_1, dict_2):
    for item in dict_2:
        dict_1[item] = dict_2[item]
    return dict_1

print(dict_merger(food_calories_1, food_calories_2))