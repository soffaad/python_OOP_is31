class Message:
    __slots__ = ('text', 'author')
    def __init__(self, text, author):
        self.text = text
        self.author = author
    def __str__(self):
        return f"{self.author}: {self.text}"

m = Message("Привет", "Анна")
print(m)