#Ingresar un numero y ver si positivo/negativo, si es posito determinar si es par o impar

numero = int(input("Ingrese un numero: "))
if numero > 0:
    print("El numero: " + str(numero) + " es positovo")
    if numero % 2 == 0:
        print("El numero: " + str(numero) + " es par")
    else:
        print(f"El numero: {numero} es impar")
else:
    print("El numero: ", numero , " es negativo")
