# Weekly task 04
# collatz.py
# Asks  user to input  positive integer and outputs successive values of the following calculation:
# if even, divide by 2; if odd, multiply by 3 and add 1
# This program shows the Collatz Conjecture problem
# Author: Rebecca Feeley
 
number = int(input("Enter a positive integer: ")) # asks user to input a number and converts it to an integer
collatz_numbers = [] # a list is created for each number to be added to

while number <= 0: # while loop created so catch any negative numbers inputted so program runs properly
    print ("The number inputted must be a positive integer.")
    number = int(input("Please enter a positive integer: "))

def collatz(number): # I created a function to carry out the calculations required by the Collatz Conjecture
    if (number % 2) == 0: # the number entered is checked using modulus to see if it is even. If it is even, 
        number = (number // 2) # this code runs and number is divided by 2 and added to collatz_numbers list
    elif (number % 2) == 1: # else if the number entered is odd,
        number = (number * 3 + 1) # this code runs and the number is multiplied by 3 and 1 is added. 
    return (number)

while number != 1: # this creates a while loop that runs until the output equals 1
    collatz_numbers.append(number) #Its appended to collatz_numbers list 
    number = collatz(number)
    # this loop continues until the number 1 is the outcome. 
    # The outputs of the if loop collatz function are appended to the collatz_numbers list
collatz_numbers.append(number)
print(*collatz_numbers) # the '*' is used to unpack the collatz_numbers list into seperate arguments and prints them out


