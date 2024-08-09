def improve_grammar(text):
    if type(text) is not str:
        raise Exception("input is not a string")
    if text == ' ':
        raise Exception("cannot improve grammar of empty text")
    return text[0] == text[0].upper() and text[-1] in '.?!'