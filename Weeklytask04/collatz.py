# collatz.py
# Asks  user to input  positive integer and outputs  successive values of the following calculation:
# if even, divide by 2; if odd, multiply by 3 and add 1
# Author: Rebecca Feeley
 
numbers = []
number = int(input("Enter a positive integer: "))

while number != 1:
    numbers.append(number)
    if (number % 2) == 0:
        number = (number // 2)
    elif (number % 2) == 1:
        number = (number * 3 + 1)
    print (number)