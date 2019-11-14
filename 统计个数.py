sstr = list(input("Please enter a string: "))

alphas = []
digits = []
spaces = []
others = []

for i in range(len(sstr)):
    if ord(sstr[i]) in range(48, 58):
        digits.append(sstr[i])
    elif ord(sstr[i]) in range(65, 91) or ord(sstr[i]) in range(97, 123):
        alphas.append(sstr[i])
    elif ord(sstr[i]) == 32:
        spaces.append(sstr[i])
    else:
        others.append(sstr[i])
print("The number of alpha is " + str(len(alphas)) + ".\n"
      + "The number of digit is " + str(len(digits)) + ".\n"
      + "The number of space is " + str(len(spaces)) + ".\n"
      + "The number of others is " + str(len(others)) + ".")


