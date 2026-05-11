def process(a: int, b: int, *args: int, **kwargs: int) -> int:
    total = a + b
    for num in args:
        total += num
    for value in kwargs.values():
        total += value
    return total

print(process(1, 2, 3, 4, x=5, y=6))