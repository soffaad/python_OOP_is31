class User:
    __slots__ = ('login', 'password')
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def change_password(self, old, new):
        if self.password == old:
            self.password = new

u = User("user", "123")
u.change_password("123", "456")
print(u.password)