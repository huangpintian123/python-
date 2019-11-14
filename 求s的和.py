n = int(input('plz input n:  '))
if n <= 0:
    print('Error!')
else:
    sum = n*(n+1)*(n+2)/6
    print('%.0f'%sum)