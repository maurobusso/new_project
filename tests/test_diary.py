from lib.diary import *

"""
give an empty string it return an empty string
"""
def test_snippet_is_empty():
    result = make_snippet("")
    assert result == ""

""" 
string with one word it return one word
"""
def test_snippert_return_one_word():
    result = make_snippet("ciao")
    assert result == "ciao"

""" 
string with 3 words return same string
"""
def test_snippet_return_a_sentence():
    result = make_snippet("ciao come stai")
    assert result == "ciao come stai"

"""test string return no more than 5 and ... if more than 5"""
def test_more_than_five_words_():
    result = make_snippet("Hello mate, how are you doing today in this fine weather")
    assert result == "Hello mate, how are you..."