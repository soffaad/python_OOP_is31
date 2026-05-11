import csv

with open('data.csv', 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

with open('filtered.csv', 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['name', 'age'])
    writer.writeheader()

    for row in rows:
        if int(row['age']) > 25:
            writer.writerow(row)

print("Отфильтрованные данные записаны в filtered.csv")