# Write a program to display the last digit of a number.

num=int(input("enter the number"))
num1=num%10
if num>0:
    print(num1,"it is last digit")
else:
    print(num1,"it is not last digit")
