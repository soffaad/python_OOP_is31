import time
from datetime import datetime

# Текущая дата и время
now = datetime.now()
timestamp = int(now.timestamp())
print(f"UNIX timestamp: {timestamp}")

# Обратно из timestamp
back_to_date = datetime.fromtimestamp(timestamp)
print(f"Обратно в дату: {back_to_date}")