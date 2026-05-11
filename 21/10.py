class Employee:
    __slots__ = ('name', 'salary')
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increase(self, percent):
        self.salary += self.salary * percent / 100

e = Employee("Анна", 50000)
e.increase(10)
print(e.salary)