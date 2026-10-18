from functools import reduce

nums = [1, 4, 5, 2, 6, 7, 23]
def sum(a, b):
    return a + b


p = int(reduce(sum, nums))

print(p)

