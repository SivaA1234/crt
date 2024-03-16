n=int(input("enter the number:"))
temp=n
count=0
sum=0
while n>0:
    count=count+1
    n=n//10
n=temp
while n>0:
    digits=n%10
    sum=sum+digits**count
    n=n//10
    count=count-1
print(sum)
