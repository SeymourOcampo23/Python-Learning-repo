def multiply(*args):
    total = 1
    for num in args:
        total *= num    
    return total

print(multiply(4, 5, 6))

def add_to_dict(**kwargs):
    dict={}
    for item in kwargs.keys():
        dict[item] = kwargs[item]
    return dict

print(add_to_dict(mike=123, john=12, lad=13))
print(add_to_dict(george=54, irwin=99, bob=100))