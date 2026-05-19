class ComplexDescriptor:
    def __init__(self, name, expected_type, min_val=None, max_val=None):
        self.name = name
        self.expected_type = expected_type
        self.min_val = min_val
        self.max_val = max_val

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f"Лог: чтение атрибута {self.name}")
        return instance.__dict__.get(f'_{self.name}')

    def __set__(self, instance, value):
        print(f"Лог: установка атрибута {self.name} = {value}")

        # Проверка типа
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} должен быть {self.expected_type.__name__}, получено {type(value).__name__}")

        # Проверка диапазона
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"{self.name} не может быть меньше {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"{self.name} не может быть больше {self.max_val}")

        instance.__dict__[f'_{self.name}'] = value

    def __delete__(self, instance):
        print(f"Лог: попытка удаления атрибута {self.name}")
        raise AttributeError(f"Удаление атрибута {self.name} запрещено")


class Person:
    age = ComplexDescriptor("age", int, 0, 120)
    name = ComplexDescriptor("name", str)


if __name__ == "__main__":
    p = Person()
    p.age = 30
    p.name = "Иван"
    print(p.age)
    print(p.name)

    try:
        p.age = 150
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        del p.age
    except AttributeError as e:
        print(f"Ошибка: {e}")