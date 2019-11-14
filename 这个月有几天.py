a = eval(input('请输入月份：'))

while not (isinstance(a, int) and 0 < a < 13):
    a = eval(input('请输入正确的月份：'))

da = [1, 3, 5, 7, 8, 10, 12]
xiao = [4, 6, 9, 11]

if (a in da):
    print(a, '月有31天')
elif (a in xiao):
    print(a, '月有30天')
else:
    n = eval(input('请输入月所在年：'))
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        print(n, '年为闰年', a, '月有29天')
    else:
        print(n, '年为平年', a, '月有28天')