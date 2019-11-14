for a in range (9+1):
    for b in range(9+1):
        i = a*11
        j = b*11
        if i !=j:
            n = i*100+j
            if int(n**(1/2))**2 ==n:
                print(n)