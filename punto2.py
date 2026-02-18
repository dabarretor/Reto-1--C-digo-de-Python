palindromo=str(input("digite una palabra: "))
palindromo = palindromo.lower().replace(" ", "")
i = 0
j = len(palindromo) - 1
while i<j:
    if palindromo[i]!=palindromo[j]:
        print("la palabra no es un palindromo: ", palindromo)
        break
    i +=1
    j -=1
else:
    print("la palabra es un palindromo: ", palindromo)