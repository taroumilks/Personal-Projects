#Day 1 of Python  
#- Peter Peng

"""Exercise 1:
Given two integer numbers return their product only if the product is 
equal to or lower than 1000, else return their sum."""    

from operator import truediv

def isAbove1000(number1,number2):
    if(number1*number2 <= 1000):
        print(number1*number2)
    else:
        print(number1+number2)

"""Exercise 2:
Write a program to iterate the first x numbers and in each iteration, 
print the sum of the current and previous number."""

def Iteration(value):
    total_sum = 0
    previous_number = 0
    for x in range(value):
        total_sum += x
        previous_number = x-1
        if(previous_number < 0):
            previous_number = 0

        print ("Current Number: " + str(x) + " Previous Number: " + str(previous_number) + " Total Sum: " + str(total_sum))


"""Exercise 3:
Write a program to accept a string from the user and display characters 
that are present at an even index number."""

def EvenIndexNumber(string):
    length = len(string)
    print("The Original Word was: " + string)
    for x in range(length):
        if(x % 2 == 0):
            print(string[x])

"""Exercise 4:
Write a program to remove characters from a string starting from zero up to n and return a new string."""

def RemovePartofWord(string,value):
    FinalString = ""
    lengthofString = len(string) 
    counter = lengthofString - value 
    for x in range(counter):
        
        FinalString = FinalString + string[value + x]
    print(FinalString)

def RemovePartofWordBetter(string,value):
    print(string[value:])

"""Exercise 5:
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False."""

def FirstandLast(List):
    Length = len(List)
    if(List[0] == List[Length-1]):
        print(True)
    else:
        print (False)

"""Exercise 6: <-- NEED TO GO BACK 
Iterate the given list of numbers and print only those numbers which are divisible by 5"""

def DivisiblebyFive(List):
    num_list = [10, 20, 33, 46, 55]
    print("Given list:", num_list)
    print('Divisible by 5:')
    for num in num_list:
        if num % 5 == 0:
            print(num)

