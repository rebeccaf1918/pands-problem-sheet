# Weekly Task 02
# bank.py
# Adding two numbers and prints out result in human readable euro currency.
# Author: Rebecca Feeley

number1 = int(input("Enter amount 1 (in cents):")) # asks user to input first amount in cents
number2 = int(input("Enter amount 2 (in cents):")) # asks user to input second amount in cents

sum = float(number1/100 + number2/100) #adds two inputted numbers and divides them by 100 to get result in euros, 
# not cents. Also, converts integer result to float.

currency = "€{:,.2f}".format(sum) #.2f formats the result to display two decimal places; converts result to Euro format
print (f"The sum of this is " + currency)


#REFERENCES:
# https://stackoverflow.com/questions/320929/currency-formatting-in-python