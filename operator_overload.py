class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    def get_sum(self):
        return f"x is {self.x} and y is {self.y}"

    def __add__(self, p): 
        return Point((self.x + p.x), (self.y + p.y))
        



p1 = Point(3, 4)
p2 = Point(4, 7)

p = p1 + p2 #operator overload using the __add__ function
print(p.get_sum())


       
