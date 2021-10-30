import pytest
from functions import *


## 1
@pytest.mark.parametrize("name", ["testing.txt", "data.dat"])

def test_openFile(capsys, name):
    try:
        openFile(name)
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == "File opened."
    except:
        with pytest.raises(FileNotFoundError):
            openFile(name)
            captured_stdout, captured_stderr = capsys.readouterr()
            assert captured_stdout.strip() == "File not found"

## 2
@pytest.mark.parametrize("first, second, equal", [(100, 10, 10), (9.5, 4.0, 2.375), ("lol", "string", "another string")])
def test_numbers(first, second, equal):
    with pytest.raises(TypeError):
        assert numbers(first, second) == equal


@pytest.mark.parametrize("Num1, Num2, equal", [("num1", "num2",10)])
def test_numbers(Num1, Num2, equal):
    with pytest.raises(TypeError):
        assert numbers(Num1, Num2) == equal

## 3
#def test_dist
## 3
@pytest.mark.parametrize("x1, y1, x2, y2, answer", [(0, 2, 0, 1, 1),(3,3,6,7,5),(2,-9,-3,3,13)] )
def test_dist(x1,y1,x2,y2,answer):
    assert dist(x1,y1,x2,y2) == answer

## 4
@pytest.mark.parametrize("word, answer", [("racecar", True), ("543212345", True), ("randomword", False), (12, False)])
def test_isPalindrome(word, answer):
    try:
        assert isPalindrome(word) == answer
    except:
        with pytest.raises(TypeError):
            assert isPalindrome(word) == answer
    


## these arent exactly working...
@pytest.mark.parametrize("first, second, equal", [(64, 8, 8), (81, 9, 9)])
def geninputs():
    inputs = ["70", "10"]

    for item in inputs:
        yield item


GEN = geninputs()


##5
def test_divide(capsys, monkeypatch,):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    try:
        divide()
        captured_stdout, captured_stderr = capsys.readouterr()
    
        assert captured_stdout.strip() == "Your numbers divided is: 7.0"
    except:
        with pytest.raises(TypeError):
            assert TypeError

##6
@pytest.mark.parametrize("number", [64, 81, 100, "banana"])
def sq(number):
    assert sq(number) == math.sqrt(number)
    
##7
#def test_greetUser():

##8
#def test_displayItem():
@pytest.mark.parametrize("numbers, index, expected", [(["goofy","goober","yeah"],"hello","wrong value"),(["Mr.","Krabs"],0,"Your item at 0 index is Mr."),([0,1,2],2,"Your item at 2 index is 2")])
def test_displayItem(capsys,numbers,index,expected):
    displayItem(numbers,index)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected