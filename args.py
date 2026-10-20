# Build sum_all(nums)
def sum_all(*nums):
    print(nums) # print nums so I can see the tuple
    return sum(nums)
# Build average(*nums) 
def average(*nums):
    print(nums) # print nums so I can see the tuple
    return sum(nums)/len(nums)

def greet_all(greeting, *names): #first argument has no asterisks so it takes the first 
    for name in names:           #positional argument while *names takes the rest   
        print(greeting, name)


print(sum_all(1,2,3,4,5))
print(average(99, 34, 44, 23, 67, 3))
greet_all("Hi", "Omar", "Hassan", "Yousef")
