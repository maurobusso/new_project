def make_snippet(str):
    arr = str.split(' ')
    if len(arr) > 5:
        result = arr[:5]
        return ' '.join(result) + '...'
    else:
        return str
