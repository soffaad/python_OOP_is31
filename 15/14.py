from datetime import datetime

birthday_str = input("Введите дату рождения (ГГГГ-ММ-ДД): ")
birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
today = datetime.now()

age_days = (today - birthday).days
print(f"Ваш возраст в днях: {age_days}")