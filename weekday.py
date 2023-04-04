# Weekly Task 05
# weekday.py
# Program that outputs whether or not today is a weekday.
# Author: Rebecca Feeley

from datetime import datetime

dt = datetime.now()
Day_Name = (dt.strftime("%A"))

Weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
Weekend = ["Saturday", "Sunday"]

if Day_Name in Weekday:
    print ("Yes, unfortunately, it is a weekday.")

else:
    print ("Yay, it is the weekend")
