#write a program to accept marks from user and check if the marks are greatr than 35 print cheating if the marks are equals to pass and less than 35 fail
marks=int(input("enter the marks"))
marks=35
if marks>35:
    print("cheating")
elif marks==35:
    print("pass")
else:
    print("fail")
