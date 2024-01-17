n=int(input("enter a number\n>>>"))

reverse=""
for i in range(len(str(n))):
    reverse=reverse+str(n)[-(i+1)]
print(f"reverse = {reverse}")