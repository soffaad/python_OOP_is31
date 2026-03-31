class Temperature:
    def __init__(self):
        self.__celsius = 0

    def set_celsius(self, c):
        self.__celsius = c

    def get_celsius(self):
        return self.__celsius

    def get_fahrenheit(self):
        return self.__celsius * 9/5 + 32

# Тест
temp = Temperature()
temp.set_celsius(25)
print(temp.get_celsius())      # 25
print(temp.get_fahrenheit())   # 77.0