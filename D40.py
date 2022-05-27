# Write a program to check whether a number entered is a three digit number or not.

num=int(input("enter the number"))
if num>=100 and num<1000:
    print("num is three digit number")
else:
    print("num is not three digit number")