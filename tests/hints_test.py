import hints

def hint_test():
    hint_len = 0
    word = 'der Flugel'
    tag = '[GER]'

    test_loop(word, hint_len, tag)


    word = 'die Schweizerin -nen'

    test_loop(word, hint_len, tag)

def test_loop(word, hint_len, tag):
    i = 0
    while i < len(word):
        hint, hint_len = hints.show_hint(hint_len, word, tag)
        print (hint)
        i += 1
    
    

if __name__ == '__main__':
    hint_test()
 
    
        
    


