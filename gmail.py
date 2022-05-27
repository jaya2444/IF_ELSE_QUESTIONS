

("create a gmail account")
first_name=input("enter the first name :")
if first_name>="a" and first_name<="z":
    print("clicl next")
    last_name=input("enter the last name :")
    if last_name>="a" and last_name<="z":
        print("click next")
        mob=int(input("enter the mobile number :"))
        if mob>=1000000000 and mob<=9999999999:
            print("click next")
            otp=int(input("enter the otp : "))
            if otp>=100000 and otp<=999999:
                print("click next")
                print("enter date of birth:-")
                month=int(input("enter the month : "))
                if month>=1 and month <=12:
                    date=int(input("enter the date : "))
                    if date >=1 and date<=31:
                        year=int(input("enter the year : "))
                        if year >=1000 and year<=9999:
                            gender=input("enter the gender : ")
                            if gender=="female"or gender=="male":
                                print("click next")
                                print("choose your email adress")
                            else:
                                ("plz enter the gender")
                        else:
                            print("plz enter the year") 
                    else:
                        print("plz enter the date")  
                else:
                    print("plz enter the month")   
            else:
                print("plz enter otp")
        else:
            print("plz enter mobile number") 
    else:
        print("plz enter last name") 
else:
     print("plz enter first name")

               