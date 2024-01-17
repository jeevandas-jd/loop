n=int(input("enter a number\n>>>"))
sum=0
st=""
for i in range(1,n+1):
    if i%2!=0:

        sum = sum + (i ** 2)
        if i!=n:
            st = st + f"{i ** 2}-"
        else:
            st = st + f"{i ** 2}"
    else:
        sum=sum-(i**2)
        if i!=n:
            st = st + f"{i**2}+"
        else:
            st = st + f"{i ** 2}"
print(f"the sum of the series = {st} = {sum}")
print(f"sum of the series up to {n} terms = {sum}")