
x,y,z = eval(input('plz input x,y,z:  \n'))
if x>y:
    x,y = y,x
if x>z:
    x,z = z,x
if y>z:
    y,z = z,y
print(x,y,z)


