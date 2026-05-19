class LengthDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Значение должно быть строкой")
        if len(value) > 10:
            raise ValueError("Строка не должна превышать 10 символов")
        instance.__dict__['_value'] = value


class MyClass:
    short_text = LengthDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.short_text = "Hello"
    print(obj.short_text)
    try:
        obj.short_text = "Слишком длинная строка"
    except ValueError as e:
        print(f"Ошибка: {e}")