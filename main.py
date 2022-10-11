class Morph:
    def __init__(self, *arg):
        self.lst = list(arg)

    def add_word(self, word):
        if word not in self.lst:
            self.lst.append(word)

    def get_words(self):
        return tuple(self.lst)

    def __eq__(self, other):
        return other in self.lst