a = input("input the word：")
b = []
for n in a :
   if "A"<= n <= "Z":
      b.append(n.lower())
   else:
      b.append(n)
print("".join(b))

