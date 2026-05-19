import json
# Проверяем, существует ли файл
import os
if os.path.exists("data.json"):
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print(data)
else:
    print("Файл data.json не найден. Сначала выполните задачу 15.")