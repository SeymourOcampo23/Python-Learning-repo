def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print("Done")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b
print(add(1, 3))

@logger
def greet(name, age, greeting=""):
    return f"{greeting}, I am {name}, I am {age} years old"

print(greet("mike", 24, "What's up"))


