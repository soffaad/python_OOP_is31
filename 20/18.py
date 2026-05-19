class NumberListDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise TypeError("Значение должно быть списком")
        for item in value:
            if not isinstance(item, (int, float)):
                raise TypeError("Список должен содержать только числа")
        instance.__dict__['_value'] = value


class Data:
    numbers = NumberListDescriptor()


if __name__ == "__main__":
    d = Data()
    d.numbers = [1, 2, 3, 4.5, 10]
    print(d.numbers)
    try:
        d.numbers = [1, "два", 3]
    except TypeError as e:
        print(f"Ошибка: {e}")