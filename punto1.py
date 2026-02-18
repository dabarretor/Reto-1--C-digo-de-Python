def opciones():
    
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    return float(input("Seleccione una opción: "))

def solicitar_numeros():
    num1=float(input ("digite un numero"))
    num2=float(input ("digite un numero"))
    return num1, num2

while True:
    opcion = opciones()
    if opcion < 1 or opcion > 5:
        print("Opción no válida. Intente de nuevo.")
        continue
    if opcion == 5:
        print("Gracias por usar el programa")
        break
    num1, num2 = solicitar_numeros()
    match opcion:
        case 1:
            res=num1+num2
            print(res)
        case 2:
            res=num1-num2
            print(res)
        case 3:
            res=num1*num2
            print(res)
        case 4:
            if num2==0:
                print("No se puede dividir por cero")
            else:
                res=num1/num2
                print(res)