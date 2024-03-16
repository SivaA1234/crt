#write a program to check the onroad price of a bike under the conditions if the price is greater than 72,000 then income taxes is 10% of actual price and insurance will be 15%
#if the price iss greater than 150k and less than 200k the tax will be 25% and insurance will be 20%
#if the price above 200k then tax will be 35% and insurance will be 28%
#otherwise mim bike will starts from 75k whose formula ap+tax+insurance
x=int(input("enter the price:"))
if x>72000 and x<15000:
    incometax=(10/100)*x
    print(incometax)
    insurance=(15/100)*x
    print(insurance)
elif x>150000 and x<200000:
    incometax=(25/100)*x
    print(incometax)
    insurance=(20/100)*x
    print(insurance)
elif x>200000:
    incometax=(35/100)*x
    print(incometax)
    insurance=(28/100)*x
    print(insurance)
else:
    print("the bike starts from 75000")
onroadPrice=(x+incometax+insurance)
print(onroadPrice)
