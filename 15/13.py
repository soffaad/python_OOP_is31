from datetime import datetime, timedelta

date_str = "2024-04-10"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# Находим сколько дней до понедельника (0 = понедельник)
days_until_monday = (7 - date_obj.weekday()) % 7
if days_until_monday == 0:
    days_until_monday = 7

next_monday = date_obj + timedelta(days=days_until_monday)
print(f"Ближайший понедельник: {next_monday.date()}")