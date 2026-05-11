with open("input.txt", "r", encoding="utf-8") as src:
    data = src.read()

with open("upper.txt", "w", encoding="utf-8") as dst:
    dst.write(data.upper())