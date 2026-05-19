class OnceDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        if '_value' in instance.__dict__:
            raise AttributeError("Изменение значения запрещено")
        instance.__dict__['_value'] = value


class MyClass:
    const = OnceDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.const = 100
    print(obj.const)
    try:
        obj.const = 200
    except AttributeError as e:
        print(f"Ошибка: {e}")