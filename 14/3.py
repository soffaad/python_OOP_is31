def sum_list(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3]))