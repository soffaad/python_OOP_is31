class Product:
    __slots__ = ('name', 'price')
    def __init__(self, name, price):
        self.name = name
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = price

p = Product("Телефон", 1000)
print(p.name, p.price)