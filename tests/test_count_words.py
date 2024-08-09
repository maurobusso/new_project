from lib.count_words import count_words

"""test if argument is empty string"""
def test_return_zero_if_arg_is_empty_string():
    assert count_words(' ') == 0

"""test if string is 1 word"""
def test_if_str_has_a_word():
    assert count_words('true') == 1

"""test if string is 2 words"""
def test_if_str_has_two_words():
    assert count_words('true false') == 2

"""test if string is 7 words"""
def test_if_str_has_more_words():
    assert count_words('true false this is are booleans values') == 7

"""test if string is letters"""
def test_if_str_has_more_words():
    assert count_words("a b c d e f g 1 23 4 6 7") == 12