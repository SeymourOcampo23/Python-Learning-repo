class Person:
    name = "Mike" #This is class attribute
    
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
    def greet(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old. Nice to meet you! I am {self.height}cm tall and {self.weight}lbs")


mike_person = Person(34, 170, 150)

print(mike_person.name)

class animal: 
    family = "mammal"

    def __init__(self, family, teeth, wings, scales):
        self.family = family
        self.teeth = teeth
        self.wings = wings
        self.scales = scales

    def show_family(self):
        return self.family


lizard = animal("Reptile", True, False, True) # Instance that the instance attribute is reptile but the class attribute is mammal

print(lizard.show_family())
print(animal.family)

