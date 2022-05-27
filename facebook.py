print("create new facebook account")
name=input("enter the name")
lastname=input("enter the last name")
if name>="A" and name<="Z" or name>="a" and name<="z":
    print("next")
    date=int(input("enter the date of birth"))
    if date>=1 and date<=31:
        print("now enter the month")
        month=int(input("enter the month"))
        if month>=1 and month<=12:
            print("now enter the year")
            year=int(input("enter the year"))
            if year>=0 and year<=2022:
                print(date,"/",month,"/",year)
                gender=input("enter the gender")
                if gender=="male" or gender=="female":
                    print("next")
                    password=int(input("enter the password"))
                    if password>=0 or password<=100:
                        print("create password")
                        number=int(input("enter mobile number"))
                        if number>=0 or number<=9:
                           print(number)
                           email_id=input("enter the email id")
                           if email_id=="jayakumawat21@gmail.com":
                              print("account created")
                           else:
                               print("invalid email")
                        else:
                            print("invalid mobile number")
                    else:
                        print("invalid password")
                else:
                    print("plz choose your gender")
            else:
                print("plz enter your yob")
        else:
            print("plz enter you birth month")
    else:
        print("plz enter your birth date")
else:
    print("enter your name")
            
                    
