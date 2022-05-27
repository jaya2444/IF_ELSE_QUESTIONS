# Write a Python program that reads two integers representing a month and day and prints the season
# for that month and day.
# a. Expected Output:
# Input the month (e.g. January, February etc.): july
# Input the day: 31
# Season is autumn

month=input("enter the month")
if month=="jan" or month=="feb" or month=="march":
    print("winter season")
elif month=="april" or month=="may" or month=="june":
    print("summer season")
elif month=="july" or month=="august" or month=="september" or month=="october" or month=="november" or month=="december":
    print("rainy season")
else:
    print("all")

