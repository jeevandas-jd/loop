n=int(input("enter a number\n>>>"))
new=""
for i in range(1,len(str(n))+1):
    new=new+str(n)[-i]
    new=new
if n==int(new):
    print("paliandrom")
else:
    print("not paliandrom")
