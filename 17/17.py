import csv

users = [
    ["Имя", "Возраст"],
    ["Alice", 25],
    ["Bob", 30]
]

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(users)
    
print("Файл users.csv создан")