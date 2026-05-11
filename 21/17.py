class Timer:
    __slots__ = ('start', 'end')
    def __init__(self, s, e):
        self.start = s
        self.end = e
    def diff(self):
        return abs(self.end - self.start)

t = Timer(10, 25)
print(t.diff())