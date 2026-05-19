class Multiplier:
    def multiply(self, a, b=None):
        if b is None:
            return a * a
        return a * b


if __name__ == "__main__":
    m = Multiplier()
    print(m.multiply(5))
    print(m.multiply(2, 3))