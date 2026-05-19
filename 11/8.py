
def check_positive(func):
    def wrapper(*args):
        if any(arg < 0 for arg in args):
            print("Error")
            return
        return func(*args)
    return wrapper

@check_positive
def multiply(a, b):
    print(a * b)

if __name__ == "__main__":
    multiply(3, 4)
    multiply(3, -1)