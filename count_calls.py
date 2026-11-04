def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        result = func(*args, **kwargs)
        count += 1
        if count == 1:
            print(f"{func.__name__} has been called once.")
        else:
            print(f"{func.__name__} has been called {count} times.")
        return result
    return wrapper

@count_calls
def add(a, b):
    return a + b

print(add(1, 4))
print(add(2, 4))
print(add(5, 10))