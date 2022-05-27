# Ask a user to tell the speed of his vehicle, if speed is more than 70kmph, ask him to pay that that much
# speed multiplied by 50rs. Like if his speed 100kmph, you need to ask him the fine(100-70)*50=? This is the fine amount he needs to pay, if his speed is not more 70, say him stay home, stay safe.


a=int(input("enter the speed"))
if a>70:
    print("pay",a*50)
elif a==100:
    print("fine",(a-70)*50)
elif a<=70:
    print("stay home,stay safe")