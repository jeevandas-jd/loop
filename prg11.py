m=int(input("enter starting number\n>>>"))
n=int(input("enter ending number\n>>>"))
ls=[]
for i in range(m,n+1):
    ls.append(i**2)

print(f"square of numbers b/n {m} and {n} = {ls}")
