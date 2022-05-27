card=input("insert the card")
print("please remove your card")
language=input("enter the Language")
if language=="english":
    print("click next")
    account_type=input("which type of account")
    if account_type=="current" or account_type=="saving":
        if account_type=="current":
          amount=(input("withdrawl or balance inquiry"))
          if amount=="withdrawl":
            pin=int(input("enter the pin"))
            if pin<=9999 and pin>=1000:
             cash=int(input("enter the amount"))
             if cash<=10000 and cash>=100:
                 reciept=input("do u want reciept")
                 if reciept=="yes":
                  print("plz collect ur cash")
                  print("collect ur reciept")
                  print("thank you for visiting")
                 else:
                       print("u will not get any reciept")
             else:
                  print("it is out of limit")
            else:
                  print("invalid")
          else:
                print("invalid")
        else:
              print("invalid")
    else:
          print("plz choose your account")
else:
    print("plz enter your language")
                       



print("insert the card")
language=input("enter your language :")
if language=="english":
    print("next")
    pin=int(input("enter your pin: "))
    if pin>=1000 and pin<=9999:
        print("next")
        accounttype=input("enter your account type :")
        if accounttype=="saving" or accounttype=="current":
            print("next")
            transtion=input("enter your transtion :")
            balance=10000
            if transtion=="withdrawl":
                withdrawl=int(input("enter your withdrawl :"))
                remain=balance-withdrawl
                print("bank balane=",remain)
            else:
                if transtion=="deposite":
                     deposite=int(input("enter your deposite: "))
                     remain=balance+deposite
                     print("bank balance=",remain)     
            reciept=input("do you want reciept: ")
            if reciept=="yes":
                print("collect your reciept")
                print("thanks for visiting") 
            else:
                print("collect your reciept")
                print("thanks for visiting")    
        else:
            print("plz choose your account : ")
    else:
       print("plz enter valid pin :")
else:
    print("plz enter language : ")

               





        
            

