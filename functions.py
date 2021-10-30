import math


## 1
## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try:
        infile = open(filename, "r")
        print("File opened.")
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

## 2
## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        number = num1 / num2
    except TypeError:
        raise TypeError("You entered the wrong type")
## 3
## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    try:
        dist = ((x2 - x1)**2) + ((y2 - y1)**2)

        dist = math.sqrt(dist)

        return dist
    except TypeError:
        print("Error")

## 4
## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    
    try:
        test = temp[::-1]
        if(test == temp):
            return True

        else:   
            return False
        
    except:
        raise TypeError("You entered the wrong type")
    

## 5
## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        div = num1 / num2

        print("Your numbers divided is:", div)
    except:
        raise ValueError("must enter an int")

## 6
## returns the squareroot of a particular number
def sq(num):
    try:
        
        number = math.sqrt(num)
        return number
    except:
        raise ValueError

## 7
## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## 8
## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    try:
        index = int(index)
        print("Your item at", index, "index is", numbers[index])
    except TypeError:
        print("wrong value")
    except ValueError:
        print("wrong value")
    except IndexError:
        print("IndexError")