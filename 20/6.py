class PositiveDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Значение должно быть положительным числом")
        instance.__dict__['_value'] = value


class MyClass:
    number = PositiveDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.number = 10
    print(obj.number)
    try:
        obj.number = -5
    except ValueError as e:
        print(f"Ошибка: {e}")