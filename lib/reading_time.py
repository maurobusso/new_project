def reading_time(text):
    if text == '':
        raise Exception("Cannot estimate empty text")
    words = text.split()
    return len(words)/ 200

