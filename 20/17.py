class CachedDescriptor:
    def __init__(self, func):
        self.func = func
        self.cached = False
        self.value = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if not self.cached:
            print("Вычисляем значение...")
            self.value = self.func(instance)
            self.cached = True
        return self.value


class MyClass:
    @CachedDescriptor
    def expensive_value(self):
        return sum(i * i for i in range(1000000))


if __name__ == "__main__":
    obj = MyClass()
    print(obj.expensive_value)
    print(obj.expensive_value)
    print(obj.expensive_value)