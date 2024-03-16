#write a func which states two arguments a and b type cast the value of second argument into a integer then multiply both the arguments
#and print the last digit of the number
def typecast(a,b):
    b=int(b)
    c=a*b
    print(c%10)
typecast(10,8.5)
    
