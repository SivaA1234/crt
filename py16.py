n=12345
s=1
while n!=0:
    digits=n%10
    s=s*digits
    n=n//10
print(s)
