class FlipFlopBell:
    def __init__(self):
        self.counter = 0

    def ring(self):
        if self.counter % 2 == 0:
            print("flip")
        else:
            print("flop")
        self.counter += 1