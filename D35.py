# Write a program to accept the cost price of a bike and display the road tax to be paid according to the
# following criteria :
# a. Cost price (in Rs)    Tax
# b. > 100000              15 %
# c. > 50000 and <= 100000 10%
# d. <= 50000              5%

cost=int(input("enter the price"))
if cost>100000:
    print(cost*15/100)
elif cost>50000 and cost<10000:
    print(cost*10/100)
elif cost<=50000:
    print(cost*5/100)
else:
    print("nothing")