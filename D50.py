# Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:
# Input a number: 6
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60


a=int(input("enter the number"))
i=1
if i<=10:
    print(a,"*",i,"=",a*1)
    print(a,"*",i+1,"=",a*2)
    print(a,"*",i+2,"=",a*3)
    print(a,"*",i+3,"=",a*4)
    print(a,"*",i+4,"=",a*5)
    print(a,"*",i+5,"=",a*6)
    print(a,"*",i+6,"=",a*7)
    print(a,"*",i+7,"=",a*8)
    print(a,"*",i+8,"=",a*9)
    print(a,"*",i+9,"=",a*10)



a=int(input("enter the number"))
if a==a:
        print(a*1)
if a==a:
        print(a*2)
if a==a:
        print(a*3)
if a==a:
        print(a*4)
if a==a:
        print(a*5)
if a==a:
        print(a*6)
if a==a:
        print(a*7)
if a==a:
        print(a*9)
if a==a:
        print(a*10)
else:
        print("all")
