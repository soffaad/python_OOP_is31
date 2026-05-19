class CounterDescriptor:
    def __init__(self):
        self.counter = 0

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.counter += 1
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        instance.__dict__['_value'] = value


class MyClass:
    attr = CounterDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.attr = "тест"
    for _ in range(5):
        print(obj.attr)
    print(f"Количество обращений: {obj.__class__.attr.counter}")