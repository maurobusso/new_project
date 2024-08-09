# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

reading_time
parameter -> string of text
return -> float number


```python
# EXAMPLE

def reading_time(text):
    """
    text will be a string type

    Should return a number of minute that it will take to read 

    Side effects:
        This function doesn't print anything or have any other side-effects
    """
    pass 
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
given empty string should raise an error
"""
extract_uppercase("") => raise errors

"""
Given less than 200 words should return 1 
"""
extract_uppercase("HELLO WORLD") => 1

"""
given more than 200 words should return the number / 200
"""
extract_uppercase("there are 400 words here") => 2 

"""
when words are not divisible by 200 just return the float
"""
extract_uppercase(" there are 300 words here") => 1.5

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
