def count_words(string):
    if string == ' ':
        return 0
    else:
        arr = string.split(' ')
        return len(arr) 