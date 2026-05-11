with open("log.txt", "r", encoding="utf-8") as log:
    for line in log:
        if "ERROR" in line:
            print(line, end="")