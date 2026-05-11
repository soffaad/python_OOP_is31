with open("input.txt", "r", encoding="utf-8") as src, open("numbered.txt", "w", encoding="utf-8") as dst:
    for i, line in enumerate(src, 1):
        dst.write(f"{i}: {line}")