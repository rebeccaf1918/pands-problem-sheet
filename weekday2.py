# weekday2.py
# Citation: pynative.com (https://pynative.com/python-get-the-day-of-week/)
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
