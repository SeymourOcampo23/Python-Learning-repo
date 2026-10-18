from functools import reduce
import time
# Write a decorator logger that prints "Function is being called" before
# the function runs. Use it to decorate a function say_hello() that prints
# # "Hello!"

def logger(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper  

@logger
def say_hello():
    print("Hello!")

say_hello()

# Write a decorator timer that calculates how long a function takes to execute.
# Test it with a function that sums numbers from 1 to 1,000,000.

def timer(func):
    def wrapper():
        
        start_time = time.perf_counter()
        result = func()
        end_time = time.perf_counter()
        exec_time = end_time - start_time
        
        print(f"{exec_time}s is how long it takes to run your code. ")
        return result
    return wrapper
    
@timer
def sum_numbers():
    total = 0
    for i in range(1, 1000001):
        total += i
    return total
print(sum_numbers())

# Getters and Setters
# Create a class Employee with a private attribute _salary .
# Use @property to define a getter for salary .
# Use @salary.setter to prevent setting negative values (print a warning
# instead).
# Create an object and test by setting positive and negative salaries

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary   

    @property
    def salary(self):
        return self._salary


    @salary.setter  
    def salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
        else:
            print("Must be greater than or equal to 0")


mike = Employee("mike", 5000)
print(mike.name)
print(mike._salary)

mike.salary = -1000
mike.salary = 10000
print(mike.salary)

# Create a class MathUtils with:
# A @staticmethod called add(a, b) that returns a + b .
# A @classmethod called description(cls) that prints "This is a
# utility class for math operations."
# Call both methods without creating an object.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")


print(MathUtils.add(4, 7))
MathUtils.description()


# Create a class Book with attributes title and author .
# Implement __str__() so that printing the object displays "Title by
# Author" .
# Implement __len__() so that len(book) returns the length of the title.
# Create two Book objects and test these methods.

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)


b = Book("Mobby Dick", "Herman Melville")
a = Book("Atomic Habits", "James Clear")

print(a)
print(b)

print(len(a))
print(len(b))


# Exception Handling and Custom Errors
# Write a program that asks the user to enter a number and handles:
# ValueError if the input is not a number
# ZeroDivisionError if you try to divide by zero
# Create a custom exception NegativeNumberError and raise it when the user
# enters a negative number.


class NegativeNumberError(Exception):
    "This is error is raised when a negative number is used by a user"

def enter_number(prompt):
    
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                raise NegativeNumberError("Enter a number that is not negative. ")
            return number

        except ValueError:
            print("Must be an integer.")

        except NegativeNumberError as e:
            print(e)


def calculator():
    while True:
        dividend = enter_number("Enter a number: ")
        divisor = enter_number("Enter your second number: ")

        try:
            result = dividend/divisor
            print(f"{result} = {dividend} / {divisor}")
        
        except ZeroDivisionError as e:
            print(e)
            continue

        again = input("Would you like to try again? y/n: ").lower().__str__()
        if again != "y":
            break

# map(), filter(), and reduce()
nums = [1, 2, 3, 4]

def square(x):
    return x ** 2

result = map(square, nums)
print(list(result))

# Use filter() to get only even numbers from [10, 11, 12, 13, 14]
nums = [10, 11, 12, 13, 14]

def is_even(x):
    if x % 2 == 0:
        return x

result = filter(is_even, nums)

print(list(result))

# Use reduce() from functools to find the product of all elements in [1, 2,
#  3, 4] .
nums = [1, 2, 3, 4]

def multiply(a, b):
    return (a * b)


total = reduce(multiply, nums)
print(total)

# Use the walrus operator to read input until the user enters "quit" . Print each
# input as it is entered

# while (command := input("Enter a command: ")) != "quit":
#     print(f"Your commad is {command}")

# Use the walrus operator in a list comprehension to store lengths of words
# from ["python", "rocks", "ai"] in a list while filtering out words shorter
# than 4 characters.

words = ["python", "rocks", "ai", "buns", "pop", "Tree", "at"]
result = [get for x in words if (get := len(x)) >= 4]
print(result)  

# Write a function sum_all(*args) that accepts any number of integers and
# returns their sum.
# Write a function print_details(**kwargs) that prints key-value pairs passed
# as arguments, for example:

def add_all(*args):
    return sum(args)

print(add_all(1, 3, 4, 1, 5, 1))

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="Seymour", job="None", earnings="0")









