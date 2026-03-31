class ShoppingList:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def get_items(self):
        return self.__items

    def clear(self):
        self.__items.clear()

# Тест
sl = ShoppingList()
sl.add_item("хлеб")
sl.add_item("молоко")
print(sl.get_items())  # ['хлеб', 'молоко']
sl.clear()
print(sl.get_items())  # []