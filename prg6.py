n=int(input("enter a number\n>>>"))
fact=1

for i in range(n):
    fact=fact*(i+1)
print(f"factorial of {n} = {n}! = {fact}")