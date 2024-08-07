def make_snippet(str):
    arr = str.split(' ')
    if len(arr) > 6:
        result = arr[:5]
        return ' '.join(result) + '...'
    else:
        return str
