# Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly
# If age does not fall in any range then display the following message: “Enter appropriate age”
# Age            Sex             wage/day
# >=18 and <30   M                700
#                F                750
# >=30 and <=40  M                800           
#                F                850

age=int(input("enter the age"))
gender=input("enter the gender")
days=int(input("enter the days"))
if age>=18 and age<30 and gender=="male":
    print("total wages",days*700) 
elif age>=18 and age<30 and gender=="female":
    print("total wages",days*750)
elif age>=30 and age<=40 and gender=="male":
    print("total wages",days*800)
elif age>=30 and age<=40 and gender=="female":
    print("total wages",days*850)
else:
    print("nothing")
