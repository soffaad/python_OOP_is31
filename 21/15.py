class BankAccount:
    __slots__ = ('balance',)
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

acc = BankAccount()
acc.deposit(100)
acc.withdraw(30)
print(acc.balance)