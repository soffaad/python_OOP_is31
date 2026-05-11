class Person:
    __slots__ = ('name',)
class Student(Person):
    __slots__ = ('grade',)

s = Student()
s.name = "Иван"
s.grade = 5
print(s.name, s.grade)