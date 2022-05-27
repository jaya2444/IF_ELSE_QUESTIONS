# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

a=input("enter the file name")
if a=="abc.java":
    print("java")
elif a=="abc.py":
    print(".py")
elif a=="power point presentation":
    print(".py")
else:
    print("wrong input for now")