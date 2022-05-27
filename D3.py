# Write a python program to check whether a number is negative, positive or zero.

number=int(input("enter the number"))
if number<0:
    print(number,"is negative number")
elif number>0:
    print(number,"is positive number")
elif number==0:
    print(number,"is zero")
else:
    print("nothing")

