import math

class Circle:
    __slots__ = ('radius',)
    def __init__(self, r):
        self.radius = r
    def area(self):
        return math.pi * self.radius**2

c = Circle(5)
print(c.area())