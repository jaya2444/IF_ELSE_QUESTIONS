print("may i go to hospital")
disco=input("ask to disko :")
if disco=="may i go to hospital":
    print("yes,take permission to t$p")
    tp=input("ask to t$p :")
    if tp=="may i go to hospital":
        print("yes,take permission to coach")
        coach=input("ask to coach :")
        if coach=="may i go to hospital":
            print("yes,go and return back before 6:30pm")
            time=eval(input("return time"))
            if time<=6.30:
                print("you reached in time")
            else:
                print("you are not on time")    
        else:
            print("no")
    else:
        print("no")
else:
    print("no")