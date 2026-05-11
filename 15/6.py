with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

longest_line = max(lines, key=len)

print(f"Длина самой длинной строки: {len(longest_line)}")
print(f"Строка: {longest_line.strip()}")