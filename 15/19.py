from datetime import datetime

message = input("Введите сообщение: ")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('log_messages.txt', 'a', encoding='utf-8') as file:
    file.write(f"[{timestamp}] {message}\n")

print("Сообщение сохранено в log_messages.txt")