
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def create_zero(cls):
        obj = cls()
        obj.value = 0
        return obj
    
    def square(self, n):
        sq = lambda x: x ** 2
        return sq(n)

c = Calculator.create_zero()
print(c.square(5))          
print(Calculator.add(2, 3))