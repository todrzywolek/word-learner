from words import Word, WordBank

class Logic:
    def __init__(self):
        self.word_list = WordBank()
        self.wrong_answers = WordBank()

    def load_file(self, filename):
        f = open(filename, 'r')
        for line in f:
            if line.find(';') != -1:
                line.rstrip()
                w = line.split(';', maxsplit=1)
                word = Word(w[0], w[1])
                self.word_list.add(word)

        f.close()


    def empty(self):
        if self.word_list.size() == self.wrong_answers.size() == 0:
            return True
        if self.word_list.size() == 0:
            self.word_list.set_list(self.wrong_answers)
            self.wrong_answer.clear()
        return False
