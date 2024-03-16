#write a program in which you take an interger input fron user if that integer if it is divible by 3 and 6 print good number if the integer is divisible 2 and 7 and print an average number
#if the integer is divisible by4or9then print awesome number else badnumber
x=int(input("enter the number:"))
if x%6==0 and x%3==0:
    print("good number")
elif x%2==0 and x%7==0:
    print("average number")
elif x%4==0 or x%9==0:
    print("awesome number")
else :
    print("bad number")
