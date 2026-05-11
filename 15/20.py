from collections import defaultdict

errors_by_day = defaultdict(int)

with open('log.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if 'ERROR' in line:
            # Извлекаем дату (первые 10 символов)
            date = line[:10]
            errors_by_day[date] += 1

# Выводим результат
for date, count in sorted(errors_by_day.items()):
    print(f"{date}: {count}")