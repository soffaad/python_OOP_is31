def average(*args: float) -> float:
    if len(args) == 0:
        return 0.0
    return sum(args) / len(args)

print(average(2, 4, 6))