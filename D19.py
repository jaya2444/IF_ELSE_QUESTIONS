# Write a python program to input basic salary of an employee and calculate its Gross salary according to
# following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%

bs=int(input("enter the salary"))
if bs<=10000:
    print(bs+bs*20/100+bs*80/100)
elif bs<20000:
    print(bs+bs*25/100+bs*90/100)
elif bs>20000:
    print(bs+bs*30/100+95/100)
else:
    print("basic salary of employees")
