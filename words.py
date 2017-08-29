import random

class Word:
    """ Word and its translation"""

    def __init__(self, word, translation):
        self.source = word
        self.translation = translation
        self._hint = 0

    def get_word(self):
        return self.source

    def get_translation(self):
        return self.translation

    def hint_info(self):
        return self._hint

    def set_hint(self, hint):
        if hint >= self._hint and hint <= len(self.source):
            self._hint = hint
        
    


class WordBank:
    """ Work as a container for all Words from a file"""

    def __init__(self):
        self.words = []

    def set_list(self, word_list):
        self.words = word_list

    def add(self, word):
        self.words.append(word)

    def remove(self, index):
        self.words.pop(index)

    def clear(self):
        self.words = []

    def size(self):
        return len(self.words)

    def get_word(self, index):
        return self.words[index]

    def random_word(self):
        index = random.randint(0, self.words.size()-1)
        word = self.remove(index)
        return word
