import pytest
from functions import *

def test_openFile():
    assert openFile("") == 6

@pytest.mark.parametrize("first, second, equal", [(100,10, 10), (144, 12, 12), ("lol","string", "another string")])
def test_numbers(first, second, equal):
    assert numbers(first, second) == equal

@pytest.mark.parametrize("word, answer", [("racecar", True), ("543212345", True), ("randomword", False), (12, False)])
def test_isPalindrome(word, answer):
    assert isPalindrome(word) == answer


## these arent exactly working...
def geninputs():
    inputs = ["64", "8", "81", "9"]

    for item in inputs:
        yield item

GEN = geninputs()

def test_divide(divider):
    divider.setattr('builtins.input', lambda _: next(GEN))

    assert divide()