# Write a Python program to test whether a number is within 100 of 1000 or 2000

a=int(input("enter the number"))
if a<100:
    print(a,"is within 100")
elif a<1000:
    print(a,"is within 1000")
elif a<2000:
    print(a,"is within 2000")
else:
    print("nothing")