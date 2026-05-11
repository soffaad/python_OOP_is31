
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

unique_lines = list(dict.fromkeys(lines))  # Сохраняет порядок

with open('unique.txt', 'w', encoding='utf-8') as file:
    file.writelines(unique_lines)

print("Уникальные строки записаны в unique.txt")