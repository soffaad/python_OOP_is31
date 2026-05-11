with open("input.txt", "r", encoding="utf-8") as src:
    with open("copy.txt", "w", encoding="utf-8") as dst:
        dst.write(src.read())