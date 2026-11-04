def apply_twice(func, value):
    return func(func(value))

def double(n):
    return n * 2

print(apply_twice(double, 4))