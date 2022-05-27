# Write a python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and
# Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

phy=int(input("enter the number"))
chem=int(input("enter the number"))
bio=int(input("enter the number"))
math=int(input("enter the number"))
com=int(input("enter the number"))
percentage=phy+chem+bio+math+com/500*100
if percentage>=90:
    print("grade A")
elif percentage>=80:
    print("grade B")
elif percentage>=70:
    print("grade C")
elif percentage>=60:
    print("grade D")
elif percentage>=40:
    print("grade E")
else:
    print("fail")


