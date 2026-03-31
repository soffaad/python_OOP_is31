class PositiveNumber:
    def __init__(self):
        self.__number = 0

    def set_number(self, n):
        if n > 0:
            self.__number = n

    def get_number(self):
        return self.__number

# Тест
pn = PositiveNumber()
pn.set_number(-5)
print(pn.get_number())  # 0
pn.set_number(10)
print(pn.get_number())  # 10