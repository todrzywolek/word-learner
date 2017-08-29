from words import Word, WordBank
import random


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

    def check_answer(self, user_input, answer):
        if user_input == self.word_list.get_word(answer).get_translation():
            return True
        return False

    def correct(self, user_input, answer, index):
        word = self.word_list.remove(index)
        if not self.check_answer(user_input, answer):
            self.wrong_answers.add(word)
            print('Wrong answer!')


    def empty(self):
        if not self.word_list:
            if self.wrong_answers:
                word_list = self.wrong_answers
                wrong_answers = []
                return True
        return False

    def rand_word(self):
        rand_index = random.randint(0, self.word_list.size())
        return self.word_list.get_word(rand_index)