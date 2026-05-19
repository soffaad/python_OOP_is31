class CounterDescriptor:
    def __init__(self):
        self.count = 0

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        instance.__dict__['_value'] = value


class ObjectCounter:
    counter = CounterDescriptor()

    def __init__(self):
        self.__class__.counter.count += 1


if __name__ == "__main__":
    print(f"Создано объектов: {ObjectCounter.counter.count}")
    a = ObjectCounter()
    b = ObjectCounter()
    c = ObjectCounter()
    print(f"Создано объектов: {ObjectCounter.counter.count}")
    d = ObjectCounter()
    print(f"Создано объектов: {ObjectCounter.counter.count}")