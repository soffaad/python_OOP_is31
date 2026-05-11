with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

count = 0
for line in lines:
    if line.strip() and line.strip()[0].isupper():
        count += 1

print(f"Количество строк, начинающихся с заглавной буквы: {count}")