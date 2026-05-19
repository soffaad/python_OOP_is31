class LoggingDescriptor:
    def __get__(self, instance, owner):
        print('Getting value')
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        instance.__dict__['_value'] = value


class MyClass:
    attr = LoggingDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.attr = 100
    print(obj.attr)