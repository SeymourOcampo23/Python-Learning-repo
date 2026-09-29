import math
import requests
from my_utils import is_even
# Defining Functions 
# Write a function greet() that prints "Hello, Python Learner!" when called.
def greet():
    print("Hello, Python Learner!")
# Write a function square(num) that returns the square of a given number. 
# Test it with different numbers.

def square(num):
    answer = num * num
    return answer
print(square(4))
print(square(3))
print(square(5))


# Write a function full_name(first, last) that takes first name and last name
# as parameters and returns a single string in the format "First Last"
def full_name(first, last):
    name = first + " "+ last
    return name

print(full_name("Seymour", "Ocampo"))

# Write a function calculate_area(length, width=10) that returns the area of
# a rectangle. Test it by calling the function with:

def calculate_area(length, width=10):
    area = length*width
    return area

print(calculate_area(25, 4))
print(calculate_area(25))

# Write a lambda function that adds two numbers and test it.
sum = lambda x, y: x + y
print(sum(4, 400))
# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get
# their squares.

numbers = [1, 2, 3, 4, 5]
foods = ["Burger", "Fried-Chicken", "Pasta", ]
square = map(lambda x: x**2, numbers)
# smaller is being interpreted as a variable because the line gives us a map object
smaller = map(lambda food: food.lower(), foods)

print(list(square))
print(list(smaller))

# Recursion
# Write a recursive function factorial(n) that returns the factorial of a
# number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(2))


def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(11324))

#  Modules and Pip – Using External Libraries
# Find the square root of 144
square_root = math.sqrt(144)
print(square_root)

# Calculate sin(90°) (hint: use math.radians() )
answer = math.sin(math.radians(90))
print(answer)
# Install and import the requests module (if available) and use it to fetch data
# from "https://api.github.com" .
r = requests.get("https://api.github.com")
print(r.text)

# Variable Scope and Docstrings
# Write a function increment() that has a local variable counter initialized to
# 0 and increments it by 1 each time it is called. Observe whether the value
# persists across function calls.
def increment():
    counter = 0
    counter += 1
    return counter

print(increment())
print(increment())
print(increment())
print(increment()) #The value of counter stays at 1 every time increment() is called


# Write a function multiply(a, b) that has a proper docstring explaining what
# it does. Then use help(multiply) to display the docstring.

def multiply(a, b):
    """Returns the result of the multiplication of the values of a and b"""
    return a * b

# Write a recursive function fibonacci(n) that prints the first n Fibonacci
# numbers.
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(2))

# Write a function safe_divide(a, b) that returns the result of a / b , but
# returns "Cannot divide by zero" if b is 0 .
def safe_divide(a, b):
    if b == 0:
        return "Cannot Divide by 0"
    return a/b
print(safe_divide(5, 0))
print(safe_divide(5, 10))

# Create a small module my_utils.py with a function is_even(n) that returns
# True if n is even. Import and use it in another Python file.

print(is_even(4))
print(is_even(5))
