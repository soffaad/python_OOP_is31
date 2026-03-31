class AlternatingCounter:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.next_is_a = True

    def count(self):
        if self.next_is_a:
            self.a += 1
        else:
            self.b += 1
        self.next_is_a = not self.next_is_a
        return (self.a, self.b)

    def reset(self):
        self.a = 0
        self.b = 0
        self.next_is_a = True