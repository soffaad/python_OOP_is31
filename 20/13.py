class RoundDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        instance.__dict__['_value'] = round(value, 2)


class MyClass:
    price = RoundDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.price = 10.4567
    print(obj.price)
    obj.price = 3.14159
    print(obj.price)