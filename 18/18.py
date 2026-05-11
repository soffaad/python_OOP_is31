with open("log.txt", "r", encoding="utf-8") as log:
    error_count = sum(1 for line in log if "ERROR" in line)
print("Количество ошибок:", error_count)