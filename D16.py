# Write a python program to check whether the triangle is equilateral, isosceles or scalene triangle.

a=int(input("enter the value"))
b=int(input("enter the value"))
c=int(input("enter the value"))
if a==b==c:
    print("equilaterial triangle")
elif a==b!=c or b==c!=a or c==a!=b:
    print("isoscale triangle")
else:
    print("scalene triangle")
    
