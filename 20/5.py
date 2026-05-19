class IntDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"Значение должно быть int, получено {type(value).__name__}")
        instance.__dict__['_value'] = value


class MyClass:
    number = IntDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.number = 42
    print(obj.number)
    try:
        obj.number = "строка"
    except TypeError as e:
        print(f"Ошибка: {e}")