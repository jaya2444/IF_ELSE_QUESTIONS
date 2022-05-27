num=int(input("enter the number"))
if num>0:
    l=num%10
    b=l
    r=num//10
    l=r%10
    c=l
    r=r//10
    d=r
    print(b,c,d,sep="")