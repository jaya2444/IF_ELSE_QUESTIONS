# Write a python program to input electricity unit charges and calculate total electricity bill according to the
# given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

num=int(input("enter the charge"))
num1=num*20/100
if num<=50:
    print(num*0.50)
elif num<=100:
    print(num*0.75)
elif num>100:
    print(num*1.20)
elif num>=250:
    print(num*1.50+num1)
else:
    print("invalid")
