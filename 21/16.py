class Temperature:
    __slots__ = ('celsius',)
    def __init__(self, c):
        self.celsius = c
    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32

t = Temperature(25)
print(t.to_fahrenheit())