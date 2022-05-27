# Write a python program to check whether a number is divisible by 5 and 11 or not.
#like 55 is divisible by 11 and 5 also.

num=int(input("enter the number"))
if num%5==0 and num%11==0:
    print("it is divisible by 5 and 11")
elif num%5==0:
    print("it is divisible by 5")
elif num%11==0:
    print("it is divisible by 11")
else:
    print("it is not divisible")
