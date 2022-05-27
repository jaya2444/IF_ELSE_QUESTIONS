# Write a Python program to find the median of three values. Go to the editor
# i.
# Expected Output:
# ii. Input first number: 15
# iii. Input second number: 26
# iv. Input third number: 29
# v. The median is 26.0

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a<c or a<b and a>c:
    print("a is medium:-",float(a))
elif b>a and b<c or b<a and b>c:
    print("b is medium:-",float(b))
elif c>a and c<b or c<a and c>b:
    print("c is medium:-",float(c))
else:
    print("nothing")