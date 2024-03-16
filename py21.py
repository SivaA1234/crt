n=int(input("enter the number:"))
b=len(str(n))
temp=n
sum=0
while n!=0:
    digit=n%10
    sum=sum+digit**b
    n=n//10
if sum==temp:
    print("amstrong")
else:
    print("not a amstrong")
