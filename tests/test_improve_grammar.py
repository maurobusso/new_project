import pytest
from lib.improve_grammar import *

"""given text that doesnt start with capitol return false"""
def test_text_doesnt_start_with_capitol():
    assert improve_grammar("hello world.") == False

"""given text that doesnt end with . return false"""
def test_text_doesnt_end_with_full_stop():
    assert improve_grammar("Hello world") == False

"""given text that doesnt end with . return false"""
def test_given_capital_and_full_stop_return_true():
    assert improve_grammar("Hello world.") == True

"""given input that is not a str raise error"""
def test_input_is_not_str():
    with pytest.raises(Exception) as error:
        improve_grammar(10)
    error_message = str(error.value)
    assert error_message == "input is not a string"

"""given empty string raise error"""
def test_input_is_empty_string():
    with pytest.raises(Exception) as error:
        improve_grammar(' ')
    error_message = str(error.value)
    assert error_message == "cannot improve grammar of empty text"

"""given different puntc mark at the end still return true"""
def test_different_punctuation_marks():
    assert improve_grammar('Hello world!!') == True