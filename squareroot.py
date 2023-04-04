# Weekly task 06
# squareroot.py
# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Rebecca Feeley

number = float(input("Please enter a positive number: ")) # asks user to input number and converts it to a float
if number <= 1: # if number is not a positive number, it reads error message and asks user to reenter a positive number.
    print ("You have not entered a positive number.") 
    number = float (input("Previous number was not positive. Please enter a positive number: "))

def sqrt(number): 
    guess_sqrt = number / 2  #square root of number must be less than half of the value of original number 
    newton_sqrt = ((guess_sqrt + (number/guess_sqrt)) * 0.5) #sqrt = (0.5(x + (n/x)))
    while guess_sqrt != newton_sqrt:
        guess_sqrt = newton_sqrt
        newton_sqrt = ((guess_sqrt + number/guess_sqrt) * 0.5)
    return guess_sqrt

print (sqrt(number))

