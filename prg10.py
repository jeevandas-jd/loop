a=int(input("enter a number\n>>>"))
tem_a=a
n=len(str(a))
sum=0
for i in range(n):
    sum=sum+((a%10)**n)
    a=a//10
if tem_a==sum:
    print(f"{tem_a} is a armstrong number")
else:
    print(f"not an armstrong number")

