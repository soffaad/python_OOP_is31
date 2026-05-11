from datetime import datetime, timedelta

start = datetime(2024, 4, 1)
end = datetime(2024, 4, 15)

workdays = 0
current = start

while current <= end:
    if current.weekday() < 5:  # 0=пн, 4=пт
        workdays += 1
    current += timedelta(days=1)

print(f"Рабочих дней между {start.date()} и {end.date()}: {workdays}")