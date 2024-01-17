n=int(input("enter a number\n>>>"))

nsqr=n*n
m=(10**len(str(n)))
r=nsqr%m
if r==n:
    print("automorphic!!")
else:
    print("not automorphic")