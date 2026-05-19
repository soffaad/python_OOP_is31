import random
import os
from datetime import datetime

# 1. Генерация 5 случайных чисел
numbers = [random.randint(1, 100) for _ in range(5)]

# 2. Добавление даты
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Запись в файл
with open("numbers.txt", "w", encoding="utf-8") as f:
    f.write(f"Дата создания: {current_date}\n")
    f.write("Случайные числа: " + ", ".join(map(str, numbers)) + "\n")

# 4. Проверка существования файла
if os.path.exists("numbers.txt"):
    print("Файл существует")
else:
    print("Файл не найден")

# 5. Чтение и вывод содержимого
print("\nСодержимое numbers.txt:")
with open("numbers.txt", "r", encoding="utf-8") as f:
    print(f.read())