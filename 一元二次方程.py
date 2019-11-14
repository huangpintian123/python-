
import math
a,b,c = eval(input('plz input 3 numbers\n'))
if a==0:
        print('Error')
else:
        t=b*b-4*a*c
        x=-b/2*a

        if t>=0:
            x1=(-b-math.sqrt(t))/(2*a)
            x2=(-b+math.sqrt(t))/(2*a)
            if x1<x2:
                print('x1=%.2f,x2=%.2f'%(x1,x2))
            else:
                print('x1=%.2f,x2=%.2f' %(x2, x1))
        else:
            print('no real root')


