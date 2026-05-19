import os

# Проверяем, существует ли файл
if os.path.exists("data.txt"):
    size = os.path.getsize("data.txt")
    print(size, "байт")
else:
    print("Файл data.txt не существует")
    # Создаём тестовый файл для демонстрации
    with open("data.txt", "w") as f:
        f.write("Hello, world!")
    size = os.path.getsize("data.txt")
    print(f"Файл создан, размер: {size} байт")