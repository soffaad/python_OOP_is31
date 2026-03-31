class EmailAccount:
    def __init__(self):
        self.__email = ""

    def set_email(self, email):
        if '@' in email:
            self.__email = email

    def get_email(self):
        return self.__email

# Тест
ea = EmailAccount()
ea.set_email("test@mail.ru")
print(ea.get_email())  # test@mail.ru
ea.set_email("wrong")
print(ea.get_email())  # test@mail.ru (не изменилось)