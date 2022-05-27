# Write a python program to count the total number of notes in a given amount.

amount=int(input("enter the amount"))
if amount%5==0:
    print("5 rupees notes",amount/5)
if amount%10==0:
    print("10 rupees notes",amount/10)
if amount%20==0:
    print("20 rupees notes",amount/20)
if amount%50==0:
    print("50 rupees notes",amount/50)
if amount%100==0:
    print("100 rupees notes",amount/100)
if amount%200==0:
    print("200 rupees notes",amount/200)
if amount%500==0:
    print("500 rupees notes",amount/500)
if amount%2000==0:
    print("2000 rupees notes",amount/2000)
else:
    print("nothing")