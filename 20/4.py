class PrivateDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_private_value')

    def __set__(self, instance, value):
        instance.__dict__['_private_value'] = value


class MyClass:
    attr = PrivateDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.attr = "секрет"
    print(obj.attr)
    print(obj.__dict__)