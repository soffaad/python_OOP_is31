class WordCaseSeparator:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def upper_case_words(self):
        return [w for w in self.words if w and w[0].isupper()]

    def lower_case_words(self):
        return [w for w in self.words if w and w[0].islower()]