with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Разбиваем на слова и приводим к нижнему регистру
words = text.lower().split()
unique_words = set(words)

print(f"Количество уникальных слов: {len(unique_words)}")