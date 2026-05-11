from datetime import datetime

deadline_str = input("Введите дату дедлайна (ГГГГ-ММ-ДД): ")
deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
today = datetime.now()

if deadline < today:
    print("Дедлайн просрочен!")
else:
    days_left = (deadline - today).days
    print(f"До дедлайна осталось {days_left} дней")