class LimitedCounter:
    def __init__(self, max_value):
        self.__max_value = max_value
        self.__value = 0

    def increment(self):
        if self.__value < self.__max_value:
            self.__value += 1

    def decrement(self):
        if self.__value > 0:
            self.__value -= 1

    def get_value(self):
        return self.__value

# Тест
lc = LimitedCounter(5)
lc.increment()
lc.increment()
print(lc.get_value())  # 2
lc.increment()
lc.increment()
lc.increment()
lc.increment()  # не сработает (лимит 5)
print(lc.get_value())  # 5
lc.decrement()
print(lc.get_value())  # 4