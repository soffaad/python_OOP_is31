class SetLoggingDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        print('Setting value')
        instance.__dict__['_value'] = value


class MyClass:
    attr = SetLoggingDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.attr = 200
    print(obj.attr)