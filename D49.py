# Write a Python program to get the next day of a given date.
# Expected Output:
# Input a year: 2016
# Input a month [1-12]: 08
# Input a day [1-31]: 23
# The next date is [yyyy-mm-dd] 2016-8-24

year=int(input("enter the year"))
month=int(input("enter the month"))
date=int(input("enter the date"))
if date>=1 and date<=31:
    print(year,"/",month,"/",date+1)
else:
    print("normal date")