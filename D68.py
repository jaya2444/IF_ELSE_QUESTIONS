# The given character is an uppercase letter or lowercase letter or a digit or a special character.



ch=input("enter the character")
if ch>="A" and ch<="Z":
    print("character is upper case")
elif ch>="a" and ch<="z":
    print("character is lower case")
elif ch=="@" or ch=="$" or ch=="#":
    print("special character")
else:
    print("digit")