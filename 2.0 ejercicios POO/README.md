# Programación Orientada a Objetos (POO) en Python
## Abstracción, Encapsulamiento, Herencia y Polimorfismo

---

# Introducción

La Programación Orientada a Objetos (POO) es un paradigma de programación que permite organizar el código mediante clases y objetos.

Los cuatro pilares fundamentales de la POO son:

1. Abstracción
2. Encapsulamiento
3. Herencia
4. Polimorfismo

---

# 1. ABSTRACCIÓN

## ¿Qué es la abstracción?

La abstracción consiste en mostrar únicamente las características importantes de un objeto y ocultar los detalles internos innecesarios.

---

# Ejemplo Básico

```python
class Televisor:

    def encender(self):
        print("Televisor encendido")

    def apagar(self):
        print("Televisor apagado")


tv = Televisor()

tv.encender()
tv.apagar()
```

---

# Explicación

El usuario solamente utiliza:
- encender()
- apagar()

No necesita conocer el funcionamiento interno.

---

# Ejercicio Resuelto

## Problema

Crear una clase `Cafetera` que permita:
- preparar café
- servir café

---

## Solución

```python
class Cafetera:

    def preparar_cafe(self):
        print("Preparando café...")

    def servir_cafe(self):
        print("Sirviendo café...")


cafetera = Cafetera()

cafetera.preparar_cafe()
cafetera.servir_cafe()
```

---

# Ejercicio para estudiantes

Crear una clase `Lavadora` con:
- lavar()
- enjuagar()
- centrifugar()

---

# 2. ENCAPSULAMIENTO

## ¿Qué es el encapsulamiento?

El encapsulamiento consiste en proteger los datos de una clase.

Python utiliza:
- _atributo → protegido
- __atributo → privado

---

# Ejemplo Básico

```python
class CuentaBancaria:

    def __init__(self):
        self.__saldo = 1000

    def mostrar_saldo(self):
        print("Saldo:", self.__saldo)


cuenta = CuentaBancaria()

cuenta.mostrar_saldo()
```

---

# Intento incorrecto

```python
print(cuenta.__saldo)
```

Resultado:

```python
AttributeError
```

---

# Ejercicio Resuelto

## Problema

Crear una clase `Alumno` donde la nota esté encapsulada.

---

## Solución

```python
class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.__nota = nota

    def mostrar_nota(self):
        print("Nota:", self.__nota)

    def cambiar_nota(self, nueva_nota):

        if 0 <= nueva_nota <= 10:
            self.__nota = nueva_nota
        else:
            print("Nota inválida")


alumno = Alumno("Carlos", 8)

alumno.mostrar_nota()

alumno.cambiar_nota(10)

alumno.mostrar_nota()
```

---

# Ejercicio para estudiantes

Crear una clase `Empleado` con:
- nombre
- sueldo privado

Métodos:
- mostrar_sueldo()
- aumentar_sueldo()

---

# 3. HERENCIA

## ¿Qué es la herencia?

La herencia permite reutilizar atributos y métodos de otra clase.

---

# Concepto visual

```text
Persona
   ↑
Estudiante
```

---

# ¿Qué es super()?

super() permite reutilizar el constructor de la clase padre.

---

# Ejemplo Correcto con super()

```python
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Estudiante(Persona):

    def __init__(self, nombre, edad, carrera):

        super().__init__(nombre, edad)

        self.carrera = carrera

    def mostrar_carrera(self):
        print("Carrera:", self.carrera)


est = Estudiante("Carlos", 20, "Software")

est.mostrar_datos()
est.mostrar_carrera()
```

---

# Explicación

super().__init__(nombre, edad)

Permite reutilizar el constructor de Persona.

---

# Ejercicio Resuelto

## Problema

Crear una clase `Vehiculo` y una clase `Auto`.

---

## Solución

```python
class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)


class Auto(Vehiculo):

    def __init__(self, marca, modelo, puertas):

        super().__init__(marca, modelo)

        self.puertas = puertas

    def mostrar_puertas(self):
        print("Puertas:", self.puertas)


auto = Auto("Toyota", "Corolla", 4)

auto.mostrar_info()
auto.mostrar_puertas()
```

---

# Ejercicio para estudiantes

Crear:
- clase `Empleado`
- clase `Programador`

La clase `Programador` debe usar:
- herencia
- super()

---

# 4. POLIMORFISMO

## ¿Qué es el polimorfismo?

Un mismo método puede comportarse de diferentes formas.

---

# Ejemplo Básico

```python
class Perro:

    def sonido(self):
        print("Guau")


class Gato:

    def sonido(self):
        print("Miau")


animal1 = Perro()
animal2 = Gato()

animal1.sonido()
animal2.sonido()
```

---

# Ejercicio Resuelto

## Problema

Crear:
- clase `Pato`
- clase `Aguila`

Cada una debe implementar:
- volar()

---

## Solución

```python
class Pato:

    def volar(self):
        print("El pato vuela bajo")


class Aguila:

    def volar(self):
        print("El águila vuela alto")


aves = [Pato(), Aguila()]

for ave in aves:
    ave.volar()
```

---

# Ejercicio para estudiantes

Crear:
- clase `Rectangulo`
- clase `Circulo`

Ambas deben implementar:
- calcular_area()

---

# EJERCICIO INTEGRADOR

## Problema

Crear un sistema de empleados aplicando:
- abstracción
- encapsulamiento
- herencia
- polimorfismo

---

# Solución Completa

```python
class Empleado:

    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.__sueldo = sueldo

    def trabajar(self):
        print("El empleado trabaja")

    def mostrar_sueldo(self):
        print("Sueldo:", self.__sueldo)


class Programador(Empleado):

    def __init__(self, nombre, sueldo, lenguaje):

        super().__init__(nombre, sueldo)

        self.lenguaje = lenguaje

    def trabajar(self):
        print("El programador desarrolla software")


class Diseñador(Empleado):

    def __init__(self, nombre, sueldo, herramienta):

        super().__init__(nombre, sueldo)

        self.herramienta = herramienta

    def trabajar(self):
        print("El diseñador crea interfaces")


empleados = [
    Programador("Ana", 1200, "Python"),
    Diseñador("Luis", 1000, "Figma")
]

for emp in empleados:

    print("Empleado:", emp.nombre)

    emp.trabajar()

    emp.mostrar_sueldo()

    print()
```

---

# Preguntas para estudiantes

1. ¿Qué es abstracción?
2. ¿Qué es encapsulamiento?
3. ¿Qué ventajas tiene la herencia?
4. ¿Qué es el polimorfismo?
5. ¿Para qué sirve super()?

---

# Recomendación para enseñar

1. Clases y objetos
2. Métodos y atributos
3. Encapsulamiento
4. Herencia
5. super()
6. Polimorfismo
7. Proyecto integrador
