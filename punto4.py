import random

cantidad = int(input("¿Cuántos números quieres? "))
rango= int(input("digite el rango que quieras para que salgan los numeros aleatorios, del uno al: "))
lista = []

for i in range(cantidad):
    num = random.randint(1, rango)
    lista.append(num)

print("esta es la lista de los numeros enteros:", lista)

def mayor_suma_consecutivos(lista):
    sumas=[]
    # Inicializamos la variable con un valor muy pequeño
    # Para que cualquier suma sea mayor
    max_suma = float('-inf')
    
    # Recorremos la lista desde el primer elemento hasta el penúltimo
    for i in range(len(lista) - 1):
        suma = lista[i] + lista[i + 1]  # sumamos elementos consecutivos
        sumas.append(suma) 
        if suma > max_suma:             # verificamos si es la mayor suma encontrada
            max_suma = suma             # si lo es, actualizamos max_suma
    return max_suma, sumas

resultado, lista_sumas = mayor_suma_consecutivos(lista)
print("Esta es la nueva lista sumando los elementos consecutivos", lista_sumas)
# Llamamos a la función y mostramos el resultado
print("La mayor suma de elementos consecutivos es:", resultado)