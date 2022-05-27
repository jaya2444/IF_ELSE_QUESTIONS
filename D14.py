# Write a python program to input angles of a triangle and check whether triangle is valid or not.

num=int(input("enter the number"))
num1=int(input("enter the number"))
num2=int(input("enter the number"))
if num+num1+num2==180:
    print("valid triangle")
else:
    print("not valid triangle")
