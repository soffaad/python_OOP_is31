import string

with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Удаляем знаки препинания
translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator)

with open('clean.txt', 'w', encoding='utf-8') as file:
    file.write(clean_text)

print("Результат записан в clean.txt")