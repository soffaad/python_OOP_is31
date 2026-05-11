class Student:
    __slots__ = ('name', 'age', 'grades')
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    def add_grade(self, g):
        self.grades.append(g)
    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

s1 = Student("Петя", 18)
s1.add_grade(5)
s1.add_grade(4)
print(f"{s1.name}: средний балл {s1.average()}")