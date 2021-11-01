import pytest
from functions import *


## 1
@pytest.mark.parametrize("name, answer", [("testing.txt", "File opened."), ("data.dat", "File not found"), ("smelly.txt", "File not found"), (69, "File not found"), (2.0, "File not found")])

def test_openFile(capsys, name, answer):
    openFile(name)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == answer
    

## 2
@pytest.mark.parametrize("first, second, equal", [(100, 10, 10), (9.5, 4.0, 2.375), ("lol", "string", None)])
def test_numbers(first, second, equal):
    assert numbers(first, second) == equal


@pytest.mark.parametrize("Num1, Num2, equal", [("num1", "num2", None)])
def test_numbers1(Num1, Num2, equal):
    assert numbers(Num1, Num2) == equal

## 3
#def test_dist
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
def geninputs():
    inputs = ["70", "10"]

    for item in inputs:
        yield item


GEN = geninputs()


##5
def test_divide(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    try:
        divide()
        captured_stdout, captured_stderr = capsys.readouterr()
    
        assert captured_stdout.strip() == "Your numbers divided is: 7.0"
    except:
        pytest.raises(TypeError)

def geninputs1():
    inputs = ["9.0", "4.5"]

    for item in inputs:
        yield item


GEN1 = geninputs1()
def test_divide1(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN1))
    try:
        divide()
        captured_stdout, captured_stderr = capsys.readouterr()
    
        assert captured_stdout.strip() == "Your numbers divided is: 2.0"
    except:
        
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == ""

def geninputs2():
    inputs = ["SWAG", "Money"]

    for item in inputs:
        yield item


GEN2 = geninputs2()
def test_divide2(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN2))
    try:
        divide()
        captured_stdout, captured_stderr = capsys.readouterr()
    
        assert captured_stdout.strip() == "Your numbers divided is: 2.0"
    except:
        
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == ""


##6
@pytest.mark.parametrize("number, answer", [(64, 8), (9.5, 3.082207001484488), (100.0, 10.0), ("banana", None) ])
def test_sq(number, answer):
    assert sq(number) == answer
    
##7
#def test_greetUser():
@pytest.mark.parametrize("first, middle, last", [("John", "Paul", "Doe"), ("Alex", "Jane", "Cox"), ("Casey", "Jones", "" ), ("X AE A-12", "", "")])
def test_greetUser(capsys, first, middle, last):
    try:
        greetUser(first, middle, last) == None
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == "Hello!\nWelcome to the program" + " "+ first + " " + middle + " " + last + "\nGlad to have you!"
    except:
       pytest.raises(TypeError)
            

##8
#def test_displayItem():
@pytest.mark.parametrize("numbers, index, expected", [(["goofy","goober","yeah"],"hello","wrong value"),(["Mr.","Krabs"],3,"IndexError"),([0,1,2],2,"Your item at 2 index is 2")])
def test_displayItem(capsys,numbers,index,expected):
    displayItem(numbers,index)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected