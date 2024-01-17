n=int(input("enter a number\n>>>"))

x=0
y=1
for i in range(n):
    print(2*y,end=" ")
    x,y=y,x+y
