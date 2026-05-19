class LogChangeDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        old = instance.__dict__.get('_value', None)
        print(f"Изменение: {old} -> {value}")
        instance.__dict__['_value'] = value


class MyClass:
    attr = LogChangeDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.attr = 10
    obj.attr = 20
    obj.attr = 30