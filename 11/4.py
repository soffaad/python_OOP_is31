
class Printer:
    def print_message(self, msg, times=1):
        for _ in range(times):
            print(msg)


if __name__ == "__main__":
    p = Printer()
    p.print_message("Hello")
    p.print_message("Hi", 3)