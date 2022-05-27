alpha=input("enter the alphabet")
digit=input("enter the digit")
spl=input("enter the special character")
if alpha >="a"and alpha<="z"or alpha>="A"and alpha<="Z":
    print("alphabet character",alpha)
    if digit>="0" and digit<="9":
        print("digit",digit)
        if spl=="@"or spl=="#"or spl=="$" or spl=="&" or spl=="*":
            print("special character",spl)
            password=alpha+digit+spl
            print(password)
            if len(password)>=8:
                print("strong password")
            else:
                 print("not strong password") 
        else:
            print("plz enter spl charater")  
    else:
        print("plz enter digit") 
else:
    print("plz enter alphabet character")