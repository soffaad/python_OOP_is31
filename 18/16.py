from datetime import datetime

with open("log.txt", "a", encoding="utf-8") as log:
    log.write(f"{datetime.now()} - Сообщение\n")