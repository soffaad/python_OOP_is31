class SafeFile:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, "r", encoding="utf-8")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("Ошибка чтения:", exc_val)
        print("File closed")
        return True  # ошибка обработана

with SafeFile("input.txt") as f:
    print(f.read())