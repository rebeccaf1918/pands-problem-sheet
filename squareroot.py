# Weekly task 06
# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Rebecca Feeley
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm


number = float(input("Please enter a positive number: "))
if number <= 1:
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