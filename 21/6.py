class Student:
    __slots__ = ('name', 'grade')
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def change_grade(self, new):
        self.grade = new

s = Student("Петя", 4)
s.change_grade(5)
print(s.grade)