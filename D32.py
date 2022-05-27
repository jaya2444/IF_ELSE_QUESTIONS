# Write a program to calculate the electricity bill (accept number of unit from user) according to the
# following criteria :
# Unit                Price
# First 100 units     no charge
# Next 100 units      Rs5 per unit
# After 200 units     Rs10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

num=int(input("enter the electricity bill"))
if num<=100:
    print("no charge")
elif num>100 and num<=200:
    print((num-100)*5)
elif num>200:
    print(((num-200)*10)+(100*5))
else:
    print("nothing")


