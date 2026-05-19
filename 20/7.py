class StringDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"Значение должно быть строкой, получено {type(value).__name__}")
        instance.__dict__['_value'] = value


class MyClass:
    text = StringDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.text = "Привет"
    print(obj.text)
    try:
        obj.text = 123
    except TypeError as e:
        print(f"Ошибка: {e}")