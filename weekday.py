# Weekly Task 05
# weekday.py
# Program that outputs whether or not today is a weekday.
# Author: Rebecca Feeley

from datetime import datetime # it is necessary to import this python module 

dt = datetime.now() # this assigns to the 'dt' variable the current date and time
day_name = (dt.strftime("%A")) # the strftime() method is used to format the datetime object as a string which represents the day of the week.
# The '%A' format code is neccessary to ensure the output is the full weekday name. 

# the following is two seperate tuples. As tuples are ordered and unchangeable, so too are the day of the week, so tuples are appropriate here.
Weekday = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
Weekend = ("Saturday", "Sunday")

if day_name in Weekday: # using an if statement, if the day_name is in the weekday tuple, it prints that it is a weekday.
    print ("Yes, unfortunately, it is a weekday.")

else: # using the else statement, if the day_name is not in the tuple, it is the weekend.
    print ("Yay, it is the weekend")
