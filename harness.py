from logic import Logic
import hints
from gui import open_file


class Harness:

    FILE_OPEN_OPTIONS = dict(defaultextension='.txt',
                             filetypes=[('text files', '*.txt')],
                             title='Wybierz plik z listą słówek')

    def __init__(self):
        self._logic = Logic()
        self._language = '[GER]'

    def start(self):
        print('Program do slowek.\nWybierz plik')
        f = open_file()
        self._logic.load_file(f)

        while not self._logic.empty():
            word = self._logic.rand_word()
            answer = word.get_translation()
            user_input = input('Your Answer: ')
            if user_input == '0':
                hints.show_hint(word.hint_info(), word.get_word(), self._language)
            else:
                self._logic.correct(user_input, answer)


        


def main():
    word_prog = Harness()
    word_prog.start()

main()

