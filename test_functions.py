import pytest
from functions import *


## 1
def test_openFile(capsys):
    openFile("testing.txt")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File opened."



## 2
@pytest.mark.parametrize("first, second, equal", [(100, 10, 10), (144, 12, 12), ("lol", "string", "another string")])
def test_numbers(first, second, equal):
    assert numbers(first, second) == equal


@pytest.mark.parametrize("Num1, Num2, equal", [("num1", "num2",10)])
def test_numbers(Num1, Num2, equal):
    assert numbers(Num1, Num2) == equal

## 4
@pytest.mark.parametrize("word, answer", [("racecar", True), ("543212345", True), ("randomword", False), (12, False)])
def test_isPalindrome(word, answer):
    assert isPalindrome(word) == answer


## these arent exactly working...
@pytest.mark.parametrize("first, second, equal", [(64, 8, 8), (81, 9, 9)])
def geninputs():
    inputs = ["70", "10"]

    for item in inputs:
        yield item


GEN = geninputs()


##5
def test_divide(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    #divider.setattr('builtins.input', lambda _: next(GEN))

    assert divide() == 7

##6
@pytest.mark.parametrize("number", [64, 81, 100, "banana"])
def sq(number):
    assert sq(number) == math.sqrt(number)
    
##7
#def test_greetUser():

##8
#def test_displayItem():
