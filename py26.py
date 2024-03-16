#-1,42,65,1,-4,6 write a program to find the second smallest negative number in the list
list=[22,-1,42,65,1,-4,6]
m1=m2=999
for x in list:
    if x<=m1:
        m1,m2=x,m1
    else:
        x=m1
print(m2)
    
