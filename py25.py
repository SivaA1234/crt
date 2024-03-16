#write a function to calculate some of first and last digit of a number
def sande(n):
    l=n%10
    while n>10:
        n=n//10
    
    print(n+l)
sande(785)
    
