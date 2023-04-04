# Weekly Task 05
# weekday.py
# Program that 
# Author: Rebecca Feeley

from datetime import datetime

dt = datetime.now() # get current datetime
x = dt.isoweekday() # get current weekday as an integer value

if x > 5: # 1 = Monday; 2 = Tuesday; etc)
    print ("It is the weekend, yay.")

else:
    print ("Yes, unfortunately, today is a weekday.")


# REFERENCES:
# https://pynative.com/python-get-the-day-of-week




