import csv
import os

# Проверяем, существует ли файл
if os.path.exists("users.csv"):
    with open("users.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
else:
    print("Файл users.csv не найден.")
    print("Сначала выполните задачу 17 для создания файла.")
    
    # Создаём файл прямо сейчас
    users = [
        ["Имя", "Возраст"],
        ["Alice", 25],
        ["Bob", 30]
    ]
    
    with open("users.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(users)
    
    print("\nФайл users.csv создан. Читаем содержимое:")
    with open("users.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)