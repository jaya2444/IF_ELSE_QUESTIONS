# Write a python program to input any character and check whether it is alphabet, digit or special
# character.

chr=input("enter the character")
if chr=="@" or chr=="#" or chr=="$" or chr=="&":
    print("is is special character")
elif chr>="a" and chr<="z" or chr>="A" and chr<="Z":
    print("it is alphabet")
else:
    print("it is digit")
