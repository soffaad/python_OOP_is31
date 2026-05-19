class DefaultDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value', 'default')

    def __set__(self, instance, value):
        instance.__dict__['_value'] = value


class MyClass:
    attr = DefaultDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    print(obj.attr)
    obj.attr = "заданное"
    print(obj.attr)