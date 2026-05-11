from datetime import datetime

dates_str = ["2024-03-15", "2024-01-10", "2024-02-20", "2024-04-01"]

# Преобразуем в объекты дат
dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates_str]
dates.sort()

sorted_dates = [d.strftime("%Y-%m-%d") for d in dates]
print(f"Отсортированные даты: {sorted_dates}")