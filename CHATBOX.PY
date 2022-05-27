chat=input("enter message :")
if chat=="hy":
    print("hello")
    chat=input("enter message")
    if chat=="how are you":
        print("i am fine")
        chat=input("enter message")
        if chat=="and you":
            print("i am also fine")
            chat=input("enter message")
            if chat=="what are you doing":
                print("nothing special")
                chat=input("enter message")
                if chat=="ok":
                    print("ok")
                else:
                    print("thik hai")  
            else:
                print("nothing")
        else:
            print("nothing")
    else:
        print("fine")
else:
    print("good morning")