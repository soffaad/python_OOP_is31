class Rectangle:
    __slots__ = ('width', 'height')
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area(self):
        return self.width * self.height

r = Rectangle(5, 10)
print(r.area())