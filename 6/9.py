class EvenOddSumTracker:
    def __init__(self):
        self.even_total = 0
        self.odd_total = 0

    def add_number(self, n):
        if n % 2 == 0:
            self.even_total += n
        else:
            self.odd_total += n

    def even_sum(self):
        return self.even_total

    def odd_sum(self):
        return self.odd_total