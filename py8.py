#write a program to check the type of triangle where you take the input from the user and classify into acoordingly into equilateral isoceles and scaling
x=int(input("enter the s1:"))
y=int(input("enter the s2:"))
z=int(input("enter the s3:"))
if x==y and y==z:
    print("it is equilateral")
elif x==y and y!=z:
    print("it is isoceles")
else:
    print("it is scaling")
