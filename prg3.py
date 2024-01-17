n=int(input("enter binary number\n>>>"))
dec=0
for i in range(len(str(n))):
    dec=dec+int(str(n)[-(i+1)])*(2**i)
print(f"decimal = {dec}")

