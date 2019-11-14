list1 = list(input('plz input liebiao:  '))
list2 = []
for i in range(len(list1)):
    a = list1.pop()
    list2.append(a)
print(list2)