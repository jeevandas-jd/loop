def happy():
    n=int(input("enter a positive intiger:"))
    it=0
    tn=(n)
    fn=(n)
    cm=n

    while it !=100:
        n = (n ** 2)
        if (n ** 2) % 10 == cm:
            print("happynumber")
            it = 100
        else:
            nd = 0
            while tn == 0:
                tn = tn // 10
                nd = nd + 1
            nwn=0
            for i in range(nd):
                nwn=nwn+((fn % 10)**2)
                fn=fn//10
            n=nwn
            it=it+1
    #print("sorry this number is sad")


import myexpiriment
myexpiriment.fib2(20)
