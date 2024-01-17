n=int(input("enter first number\n>>>"))
m=int(input("enter second number\n>>>"))
gcd=0
if m>n:
    for i in range(m):
        if m%(i+1)==0 and n%(i+1)==0:
            gcd=i+1
else:
    for i in range(n):
        if m%(i+1)==0 and n%(i+1)==0:
            gcd=i+1
print(gcd)


