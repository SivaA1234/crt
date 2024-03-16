x=int(input("enter the number:"))
n1=x
s=0
while x!=0:
    digit=x%10
    s=s+digit
    x=x//10
if n1%s==0:
    print("yes")
else:
    print("no")
