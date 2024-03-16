sof=0
sod=0
for i in range(1,31):
    if i%6==0:
        sof=sof+i
    else:
        sod=sod+i
x=sod-sof
print(x)
    
    
