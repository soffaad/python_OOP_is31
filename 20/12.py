class AgeDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Возраст должен быть числом")
        if not (0 <= value <= 120):
            raise ValueError("Возраст должен быть в диапазоне от 0 до 120")
        instance.__dict__['_value'] = value


class Person:
    age = AgeDescriptor()


if __name__ == "__main__":
    p = Person()
    p.age = 25
    print(p.age)
    try:
        p.age = 150
    except ValueError as e:
        print(f"Ошибка: {e}")