class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Тест
ba = BankAccount()
ba.deposit(1000)
ba.withdraw(300)
print(ba.get_balance())  # 700
ba.withdraw(800)  # не хватает, не снимает
print(ba.get_balance())  # 700