with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()
    word_count = len(text.split())
print("Количество слов:", word_count)