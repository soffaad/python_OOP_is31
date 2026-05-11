with open("input.txt", "r", encoding="utf-8") as f:
    line_count = sum(1 for _ in f)
print("Количество строк:", line_count)