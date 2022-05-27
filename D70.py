# Write a program to do the following operations :
# Read any two positive integer numbers (say n1 & n2) and one character type operator (say opr). Note that opr is
# any mathematical operator.
# Depending upon the operator, do the appropriate operation. e. g. if opr is ‘+’ then the display the value
# obtained by evaluating the expression (n1 + n2).


n1=int(input("enter the value"))
n2=int(input("enter the value"))
op=input("enter the operator")
if op=="+":
    print("value",n1+n2)
elif op=="-":
    print("value",n1-n2)
elif op=="*":
    print("value",n1*n2)
elif op=="/":
    print("value",n1/n2)
elif op=="//":
    print("value",n1//n2)
elif op=="%":
    print("value",n1%n2)
else:
    print("operator is invalid")