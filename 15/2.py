
from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.lower().split()
word_count = Counter(words)


sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(f"{word}: {count}")