class NumberDivider:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def divisible(self):
        return [x for x in self.numbers if x % 3 == 0]

    def not_divisible(self):
        return [x for x in self.numbers if x % 3 != 0]