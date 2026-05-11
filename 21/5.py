class Book:
    __slots__ = ('title', 'author')
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def info(self):
        return f"{self.author}: {self.title}"

b = Book("Война и мир", "Толстой")
print(b.info())