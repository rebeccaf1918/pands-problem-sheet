# accounts.py
# reads in a 10 character account number and outputs the account 
# number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: Rebecca Feeley

account_number_to_input = str(input("Enter a 10 digit account number: "))

#https://www.w3schools.com/python/ref_string_rjust.asp - I used this as inspiration for the code
account_number = (account_number_to_input[6: ].rjust(len(account_number_to_input), "X"))

print (account_number)



