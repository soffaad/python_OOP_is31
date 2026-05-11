
import csv

with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    ages = [int(row['age']) for row in reader]

average_age = sum(ages) / len(ages)
print(f"Средний возраст: {average_age}")