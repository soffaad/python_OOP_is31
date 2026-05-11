class Order:
    __slots__ = ('items',)
    def __init__(self, items):
        self.items = items
    def total(self):
        return sum(self.items)

o = Order([100, 200, 50])
print(o.total())