# Take the age of 3 people by user and determine oldest and youngest among them

a=int(input("enter the age"))
b=int(input("enter the age"))
c=int(input("enter the age"))
if a>b and a>c:
    print(a,"a is older")
elif b>a and b>c:
    print(b,"b is older")
elif c>a and c>b:
    print(c,"c is older")
if a<b and a<c:
    print(a,"a is younger")
elif b<a and b<c:
    print(b,"b is younger")
else:
    print(c,"c is younger")