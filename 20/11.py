class EmailDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_value')

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Email должен быть строкой")
        if '@' not in value:
            raise ValueError("Email должен содержать символ '@'")
        instance.__dict__['_value'] = value


class User:
    email = EmailDescriptor()


if __name__ == "__main__":
    u = User()
    u.email = "test@example.com"
    print(u.email)
    try:
        u.email = "invalid-email"
    except ValueError as e:
        print(f"Ошибка: {e}")