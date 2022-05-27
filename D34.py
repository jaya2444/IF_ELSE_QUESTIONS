# Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.

num=int(input("enter the number"))
num1=num%10
if num1%3==0:
    print(num1,"it is divisible by 3")
else:
    print("it is not divisible by 3")