# Accept the number of days from the user and calculate the charge for library according to following :
# First five days : Rs 2/day.
# Six to ten days : Rs 3/day.
# Ten to 15 days : Rs 4/day
# After 15 days : Rs 5/day

days=int(input("enter the number"))
if days<=5:
    print(days*2)
elif days>=6 and days<=10:
    print(days*3)
elif days>=10 and days<=15:
    print(days*4)
elif days>15:
    print(days*5)
else:
    print("nothing")