from logic import Logic
import hints
from gui import open_file


FILE_OPEN_OPTIONS = dict(defaultextension='.txt',
                         filetypes=[('text files', '*.txt')],
                         title='Choose word-list file')

class Harness:
    def __init__(self):
        self._logic = Logic()
        self._language = '[GER]'

    def start(self):
        print('Program do slowek.\nWybierz plik')
        f = open_file(FILE_OPEN_OPTIONS)
        self._logic.load_file(f)

        while not self._logic.empty():
            word = self._logic.word_list.random_word()
            print(word.translation)
            while True:
                user_input = input('Your Answer: ')
                if user_input == '0':
                    h, idx = hints.show_hint(word.hint_info(), word.get_word(), self._language)
                    word.set_hint(idx)
                    print(h)
                    continue
                if word.match(user_input):
                    print('OK\n')
                else:
                    print('Wrong! Correct answer: {}\n'.format(word.source))
                break


        


def main():
    word_prog = Harness()
    word_prog.start()

main()

