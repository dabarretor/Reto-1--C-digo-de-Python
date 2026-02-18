import random

cantidad = int(input("¿Cuántos números quieres? "))

lista = []
def es_primo(num):
    if num<=1:
        return False
    for i in range (2, num):
        if num % i == 0:
            return False
    return True
for i in range(cantidad):
    num = random.randint(1, 100)
    lista.append(num)
print("esta es la lista de los numeros enteros: ", lista)

primos=[]
for num in lista:
    if es_primo(num):
        primos.append(num)
print("esta es la lista de los numeros primos, tomando como referencia la anterior lista: ", primos)