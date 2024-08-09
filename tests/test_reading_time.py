import pytest
from lib.reading_time import *

"""given text of 200 words return 1"""
def test_reading_time_of_200_words_text():
    text = ' '.join(["word" for i in range(0,200)])
    result = reading_time(text) 
    assert result == 1.0

"""given text of 400 words return 1"""
def test_reading_time_of_400_words_text():
    text = ' '.join(["word" for i in range(0,400)])
    result = reading_time(text) 
    assert result == 2.0

"""given text of 300 words return 1"""
def test_reading_time_of_300_words_text():
    text = ' '.join(["word" for i in range(0,300)])
    result = reading_time(text) 
    assert result == 1.5

"""given empty text will raise an error"""
def test_reading_time_of_300_words_text():
    with pytest.raises(Exception) as error:
        reading_time('')
    error_messgae = str(error.value)
    assert error_messgae == "Cannot estimate empty text"