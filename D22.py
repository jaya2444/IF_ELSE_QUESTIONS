# A company decided to give a bonus of 5% to an employee if his/her year of service is more than 5
# years. Ask users for their salary and year of service and print the net bonus amount.

salary=int(input("enter salary"))
yos=int(input("year of salary"))
if yos>5:
    print("bonus",salary*5/100)
    print("net bonus amount",salary+(salary*5/100))
else:
    print("no bonus")