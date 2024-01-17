n=int(input("enter a number\n>>>"))

sum=0
fac=[]
for i in range(n):
    if n%(i+1)==0:
        sum=sum+(i+1)
        fac.append(i+1)
print(f"factors of the number{n} = {fac}\nsum of factors of the number {n} = {sum}")