class SecretNumber:
    def __init__(self):
        self.__number = None

    def set_number(self, n):
        self.__number = n

    def get_number(self):
        return self.__number

# Тест
sn = SecretNumber()
sn.set_number(100)
print(sn.get_number())