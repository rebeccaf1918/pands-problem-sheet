# bank.py
# Adding two numbers and prints out result in currency
# Author: Rebecca Feeley

number1 = int(input("Enter amount 1 (in cents):"))
number2 = int(input("Enter amount 2 (in cents):"))

sum = float (number1/100 + number2/100)

currency = "€{:,.2f}".format(sum)
print (f"The sum of this is " + currency)