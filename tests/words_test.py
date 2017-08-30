from words import Word, WordBank
def words_test():

    word1 = 'trocken'
    translation1 = 'sucho'
    word2 = 'er'
    translation2 = 'on'

    w1 = Word(word1, translation1)
    w2 = Word(word2, translation2)

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
    assert wb.size() == 1
    wb.add(w2)
    assert wb.size() == 2
    print(wb.random_word().get_word())
    assert wb.size() == 1
    print(wb.random_word().get_word())
    assert wb.size() == 0
    
    
        
    

    

if __name__ == '__main__':
    words_test()
 
