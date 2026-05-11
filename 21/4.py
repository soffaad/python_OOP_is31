class Car:
    __slots__ = ('brand', 'model', 'year')
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

c = Car("Toyota", "Camry", 2022)
print(c.brand, c.model, c.year)