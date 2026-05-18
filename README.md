# Taller de Python – Tipos de Datos, Funciones, IF, FOR y MATCH

## Objetivo

Practicar los conceptos básicos de Python mediante ejercicios relacionados con:

- Tipos de datos
- Variables
- Funciones
- Condicionales `if`
- Ciclos `for`
- Estructura `match-case` (switch)

---

# 1. Datos personales

## Explicación
Crear variables y mostrar información.

## Código

```python
nombre = "Byron"
edad = 20
estatura = 1.75
estudiante = True

print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("¿Es estudiante?:", estudiante)
```

---

# 2. Operaciones matemáticas

## Código

```python
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)
```

---

# 3. Conversión de tipos

## Código

```python
edad = input("Ingrese su edad: ")

edad = int(edad)

print("Tu edad es:", edad)
```

---

# 4. Promedio de notas

## Código

```python
nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print("Promedio:", promedio)
```

---

# 5. Área de un triángulo

## Fórmula

A = (b * h) / 2

## Código

```python
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

area = (base * altura) / 2

print("Área:", area)
```

---

# 6. Función sin parámetros

## Código

```python
def saludar():
    print("Bienvenido a Python")

saludar()
```

---

# 7. Función con parámetros

## Código

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Byron")
```

---

# 8. Función con retorno

## Código

```python
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 5)

print("Resultado:", resultado)
```

---

# 9. Uso de IF

## Código

```python
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

---

# 10. IF con notas

## Código

```python
nota = float(input("Ingrese la nota: "))

if nota >= 7:
    print("Aprueba")
else:
    print("Reprueba")
```

---

# 11. IF anidado

## Código

```python
numero = int(input("Ingrese un número: "))

if numero > 0:
    print("Positivo")

    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

else:
    print("Número negativo")
```

---

# 12. Uso de FOR

## Código

```python
for i in range(1, 6):
    print(i)
```

---

# 13. Tabla de multiplicar con FOR

## Código

```python
numero = int(input("Ingrese un número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
```

---

# 14. Suma de números con FOR

## Código

```python
suma = 0

for i in range(1, 6):
    suma = suma + i

print("Resultado:", suma)
```

---

# 15. Recorrer una cadena

## Código

```python
nombre = "Python"

for letra in nombre:
    print(letra)
```

---

# 16. Uso de MATCH CASE (Switch)

## Código

```python
opcion = int(input("Seleccione una opción: "))

match opcion:
    case 1:
        print("Guardar")

    case 2:
        print("Editar")

    case 3:
        print("Eliminar")

    case _:
        print("Opción incorrecta")
```

---

# 17. Calculadora con MATCH CASE

## Código

```python
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Seleccione opción: "))

match opcion:

    case 1:
        print("Resultado:", num1 + num2)

    case 2:
        print("Resultado:", num1 - num2)

    case 3:
        print("Resultado:", num1 * num2)

    case 4:
        print("Resultado:", num1 / num2)

    case _:
        print("Opción inválida")
```

---

# 18. Función + FOR

## Código

```python
def tabla(numero):

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

tabla(5)
```

---

# 19. Función + IF

## Código

```python
def mayor_edad(edad):

    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"

print(mayor_edad(20))
```

---

# 20. Sistema Integrador

## Código

```python
def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3

nombre = input("Nombre: ")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = calcular_promedio(n1, n2, n3)

print("Estudiante:", nombre)
print("Promedio:", promedio)

if promedio >= 7:
    print("Aprueba")
else:
    print("Reprueba")
```

---

# Ejercicios Propuestos

1. Crear una función para calcular el área de un círculo.
2. Mostrar los números pares del 1 al 100 usando `for`.
3. Crear un menú usando `match-case`.
4. Validar usuario y contraseña usando `if`.
5. Crear una tabla de multiplicar usando funciones.
6. Contar cuántas vocales tiene una palabra.
7. Crear una calculadora básica.
8. Mostrar el factorial de un número usando `for`.
9. Crear una función que determine si un número es primo.
10. Crear un sistema simple de cajero automático.

---

# Recomendaciones

Antes de programar:

1. Identificar entradas.
2. Identificar procesos.
3. Identificar salidas.
4. Pensar si necesita:
   - IF
   - FOR
   - Funciones
   - MATCH CASE
