# A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000. Ask the user
# for quantity, Suppose, one unit will cost 100. Judge and print total cost for user.

cost=int(input("enter the cost"))
if cost>1000:
    print("10 percent discount",cost*10/100)
    print("total cost",cost-cost*10/100)
else:
    print("no discount")
