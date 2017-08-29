from words import Word, WordBank
def words_test():

    word = 'trocken'
    translation = 'sucho'

    w1 = Word(word, translation)

    print(w1.get_word())
    print(w1.get_translation())
    print(w1.hint_info())

    print(w1.set_hint(2))
    print(w1.hint_info())

    print(w1.set_hint(-5))
    print(w1.hint_info())
    
    print(w1.set_hint(9))
    print(w1.hint_info())

    wb = WordBank()
    wb.add(w1)
    print(wb.size())
    wb.remove(0)
    print(wb.size())
    
        
    

    

if __name__ == '__main__':
    words_test()
 
