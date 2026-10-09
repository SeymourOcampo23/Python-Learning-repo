class Animal: 
    family = "mammal"

    def __init__(self, family, teeth, wings, scales):
        self.family = family
        self.teeth = teeth
        self.wings = wings
        self.scales = scales

    def show_family(self):
        return self.family

    def speak(self):
        print("Shriek")


class Cat(Animal):
    def speak(self):
        super().speak() #using super(), the child object is able to call 
        # methods from a parent/sibling class without rewriting its code. 
        print("Meowwww!")


kai = Cat("Mammal", True, False, False)
kai.speak()

