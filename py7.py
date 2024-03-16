#check in if the condition is leap year or not
#if the year is divisible by 4 and not divisible by 100 0r and if it is divisible by 400 then it is called leap year
year=int(input("enter the year:"))
if year%4==0 and year%100!=0:
    print("leap year")
elif year%400==0:
    print("leap year")
else:
    print("non leapyear")
