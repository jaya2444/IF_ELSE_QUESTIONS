# Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16

num1=int(input("enter the number"))
num2=int(input("enter the numbe"))
op=input("enter the operator")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
elif op=="%":
    print(num1%num2)
elif op=="//":
    print(num1//num2)
else:
    print("enter the correct operators")



 