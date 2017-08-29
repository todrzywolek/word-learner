
def detect_language(language_tag):
    switcher = {
        '[GER]': hint_german
        }
    return switcher.get(language_tag, hint)


def show_hint(hint_len, word, tag):
    if hint_len < len(word):
        hint_len += 1
        hint_type = detect_language(tag)

        return hint_type(hint_len, word), hint_len

    return 'You have uncovered all letters', hint_len


def hint_german(hint_len, word):
    split_word = word.split()
    hint_text = ''
    for w in split_word:
        if w[0] == '-' :
            hint_text += "+(-Pl.)"
        elif w in ['der','die','das','dem','den','des']:
            hint_text += "(Artikel) "
        else:
            hint_text += hint(hint_len, w) + ' '
    return hint_text

def hint(hint_len, word):
    covered = len(word) - hint_len
    return word[:hint_len] + covered * '*'
        
 
    
        
    


