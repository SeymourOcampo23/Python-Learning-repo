# Write a function greet(name) that returns "Hello, <name>!". 
# Then print the result outside the function.

count = 0 #global variable
def greet(name):
    return f"Hello {name}!"

print(greet("Bob"))

def print_count():
    count = 10 #local variable inside the function
    print(count)

print(count) #prints 0
print_count() #prints 10


square = lambda n: n ** 2 #lamba function that returns its square
print(square(5))

fruits = ["pear", "fig", "banana", "apple"]

print(sorted(fruits, key=lambda w:len(w))) #sort by len of the word, shortest to longest
print(sorted(fruits, key=lambda w:w[-1]))  #sort by last letter of the words in fruits

people = [("Carl", 25), ("Ben", 31), ("Ara", 25), ("Dan", 19)]

def people_sorter(people): 
    new_list = []
    for person in people:
        pair = (person[0], person[1]*-1)
        new_list.append(pair)
    new_list = sorted(new_list, key=lambda age:(age[1],age[0]))
    final_list = []
    for item in new_list:
        pair = (item[0], item[1]*-1)
        final_list.append(pair)
    return final_list

def people_sorter_lambda(people): 
    return sorted(people, key=lambda p:(-p[1], p[0]))

print(people_sorter(people)) #comparing outputs
print(people_sorter_lambda(people))
    






