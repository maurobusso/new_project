## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Function Signature

def improve_grammar():
    takes a text as input 
    return true or false
        if it starts with capital and end with .

## 3. Create Examples as Tests

given text that doesnt start with capital return false
improve_grammar('hello world.') => False

given text that doesnt end with . return false
improve_grammar('Hello world') => False

given text that start with capital end with . return true
improve_grammar('Hello world.') => True

given empty text raise error 
improve_grammar('') => "cannot improve grammar of empty text"

given parameter that is not a str rais an error
imrove_grammar(10) => "input is not a string"