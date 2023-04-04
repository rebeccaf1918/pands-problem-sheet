# Weekly task 06
# squareroot.py
# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Rebecca Feeley

number = float(input("Please enter a positive number: ")) # asks user to input number and converts it to a float, storing it in variable 'number'
if number <= 1: # if number is not a positive number, it reads error message and asks user to reenter a positive number.
    print ("You have not entered a positive number.") 
    number = float (input("Previous number was not positive. Please enter a positive number: "))

def sqrt(number): # I defined the sqrt function and it takes 1 argument i.e 'number'
    guess_sqrt = number / 2  #square root of number must be less than half of the value of original number; 
    # as Newton's method requires a guess, I equalled the guess to half the inputted number.
    newton_sqrt = ((guess_sqrt + (number/guess_sqrt)) * 0.5) #sqrt = (0.5(x + (n/x))) 
    # the above code line assigns a new newton_sqrt variable as an improved guess by using Newton's method
    while guess_sqrt != newton_sqrt: # a while loop is used to continute until the improved guess(newton_sqrt) and current guess are equal. 
        guess_sqrt = newton_sqrt # this assigns the current guess(guess_sqrt) to be equal to the improved guess
        newton_sqrt = ((guess_sqrt + number/guess_sqrt) * 0.5) # this code line uses Newton's method to get an improved guess of the square root
    return guess_sqrt

print (sqrt(number))

