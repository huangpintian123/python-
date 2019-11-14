list1 = eval(input('plz input list1:  \n'))
list2 = eval(input('plz input list2:  \n'))

list1.sort()
list2.sort()
result = []

while list1 and list2:
    if list1[0] < list2[0]:
        result.append(list1[0])
        list1.remove(list1[0])
    else:
        result.append(list2[0])
        list2.remove(list2[0])


for i in list2:
    result.append(i)
print(result)
