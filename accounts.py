# Weeklyl Task 03
# accounts.py
# reads in a 10 character account number and outputs the account 
# number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: Rebecca Feeley

account_number_to_input = str(input("Enter a 10 digit account number: ")) # asks user to input a/c number and 
#converts inputted a/c number to string format

while len(account_number_to_input) != 10: #displays an error message if a/c number entered is less than 10 digits
    print ("Account number must be 10 digits long.") # while loop continues until 10 digit a/c number entered
    account_number_to_input = str(input("Please enter a 10 digit account number: ")) # asks user to reinput a/c number

account_number = (account_number_to_input[6: ].rjust(len(account_number_to_input), "X"))
#rjust method is a built in string method in Python that adds X's for each number up to the last four digits
# so that the string is the same length as the number inputted but the first 6 digits are replaced with 'X'

print (account_number) # prints out redacted account number showing only last 4 digits

#REFERENCES:
# https://www.w3schools.com/python/ref_string_rjust.asp - # I used this as inspiration for the code
# https://stackoverflow.com/questions/59342854/how-to-mask-input-and-display-the-last-4-digit-using-python
# https://www.codingem.com/python-how-to-ask-for-user-input/

