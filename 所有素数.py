a,b=eval(input('input x and y\n'))
l = []
for n in range(a,b+1):
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        l.append(n)
print(l)

