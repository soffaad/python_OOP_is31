with open("input.txt", "r", encoding="utf-8") as src, open("no_empty.txt", "w", encoding="utf-8") as dst:
    for line in src:
        if line.strip():
            dst.write(line)