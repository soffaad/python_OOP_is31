class FullNameDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_full_name')

    def __set__(self, instance, value):
        instance.__dict__['_full_name'] = value
        if hasattr(instance, 'first_name') and hasattr(instance, 'last_name'):
            parts = value.split()
            if len(parts) >= 2:
                instance.first_name = parts[0]
                instance.last_name = parts[-1]


class Person:
    full_name = FullNameDescriptor()

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"


if __name__ == "__main__":
    p = Person("Иван", "Петров")
    print(f"Имя: {p.first_name}, Фамилия: {p.last_name}")
    p.full_name = "Алексей Сидоров"
    print(f"Имя: {p.first_name}, Фамилия: {p.last_name}")