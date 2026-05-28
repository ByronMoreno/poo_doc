# 🧠 Taller de Programación Orientada a Objetos (POO) en Python

---

# 🎯 Objetivo del Taller

Comprender los fundamentos de la Programación Orientada a Objetos mediante ejercicios prácticos en Python, aplicando:

- Clases
- Objetos
- Métodos
- Atributos
- Encapsulamiento
- Herencia
- Polimorfismo

---

# 📘 ¿Qué es la Programación Orientada a Objetos?

La Programación Orientada a Objetos (POO) es un paradigma de programación que permite representar elementos del mundo real mediante objetos.

Un objeto tiene:

| Elemento | Descripción |
|---|---|
| Atributos | Características del objeto |
| Métodos | Acciones o comportamientos |

## ✅ Ejemplo del mundo real

| Objeto | Atributos | Métodos |
|---|---|---|
| Auto | color, marca | acelerar(), frenar() |
| Estudiante | nombre, edad | estudiar(), saludar() |
| Celular | marca, modelo | llamar(), apagar() |

---

# 🧱 Clase y Objeto

## ✅ Clase

Es una plantilla o molde para crear objetos.

## ✅ Objeto

Es una instancia creada a partir de una clase.

---

# 💻 Ejemplo Básico

```python
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)


# Crear objeto
persona1 = Persona("Byron", 37)

# Usar método
persona1.saludar()
```

---

# 🔍 Explicación

| Elemento | Explicación |
|---|---|
| class Persona | Define la clase |
| __init__ | Constructor |
| self | Hace referencia al objeto |
| self.nombre | Atributo |
| saludar() | Método |
| Persona("Byron", 37) | Creación del objeto |

---

# 🧪 EJERCICIOS PRÁCTICOS

---

# ✅ EJERCICIO 1 — Clase Animal

## 📌 Enunciado

Crear una clase llamada `Animal` con:

- atributo: nombre
- método: hacer_sonido()

Mostrar el mensaje:

```python
"El animal hace un sonido"
```

---

## 💡 Solución

```python
class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido")


animal1 = Animal("Perro")

animal1.hacer_sonido()
```

---

# ✅ EJERCICIO 2 — Clase Vehículo

## 📌 Enunciado

Crear una clase `Vehiculo` con:

- marca
- color
- método mostrar_datos()

---

## 💡 Solución

```python
class Vehiculo:

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def mostrar_datos(self):
        print("Marca:", self.marca)
        print("Color:", self.color)


v1 = Vehiculo("Toyota", "Rojo")

v1.mostrar_datos()
```

---

# ✅ EJERCICIO 3 — Cuenta Bancaria

## 📌 Enunciado

Crear una clase `CuentaBancaria` con:

- titular
- saldo

Métodos:

- depositar()
- retirar()
- mostrar_saldo()

---

## 💡 Solución

```python
class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):

        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print("Saldo:", self.saldo)


cuenta = CuentaBancaria("Byron", 100)

cuenta.depositar(50)

cuenta.retirar(30)

cuenta.mostrar_saldo()
```

---

# 🔒 Encapsulamiento

Permite proteger atributos para que no puedan modificarse directamente.

Se usa `_` o `__`.

---

# 💻 Ejemplo

```python
class Usuario:

    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.__clave = clave


usuario1 = Usuario("admin", "12345")

# ERROR
# print(usuario1.__clave)
```

---

# ✅ EJERCICIO 4 — Encapsulamiento

## 📌 Enunciado

Crear una clase `Empleado` con:

- nombre
- sueldo privado

Crear método para mostrar sueldo.

---

## 💡 Solución

```python
class Empleado:

    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.__sueldo = sueldo

    def mostrar_sueldo(self):
        print("Sueldo:", self.__sueldo)


e1 = Empleado("Carlos", 900)

e1.mostrar_sueldo()
```

---

# 👨‍👦 Herencia

Permite reutilizar código entre clases.

---

# 💻 Ejemplo

```python
class Persona:

    def saludar(self):
        print("Hola")


class Estudiante(Persona):

    def estudiar(self):
        print("Estoy estudiando")


e1 = Estudiante()

e1.saludar()

e1.estudiar()
```

---

# ✅ EJERCICIO 5 — Herencia

## 📌 Enunciado

Crear:

- Clase `Animal`
- Clase `Perro`

El perro debe heredar de Animal.

---

## 💡 Solución

```python
class Animal:

    def comer(self):
        print("El animal está comiendo")


class Perro(Animal):

    def ladrar(self):
        print("Guau Guau")


p1 = Perro()

p1.comer()
p1.ladrar()
```

---

# 🎭 Polimorfismo

Permite que diferentes clases tengan métodos con el mismo nombre.

---

# 💻 Ejemplo

```python
class Gato:

    def sonido(self):
        print("Miau")


class Perro:

    def sonido(self):
        print("Guau")


g1 = Gato()
p1 = Perro()

g1.sonido()
p1.sonido()
```

---

# ✅ EJERCICIO 6 — Polimorfismo

## 📌 Enunciado

Crear:

- Clase Ave
- Clase Vaca

Ambas deben tener método sonido().

---

## 💡 Solución

```python
class Ave:

    def sonido(self):
        print("Pío pío")


class Vaca:

    def sonido(self):
        print("Muuu")


a1 = Ave()
v1 = Vaca()

a1.sonido()
v1.sonido()
```

---

# 🚀 EJERCICIOS PROPUESTOS

## 🟢 Básicos

1. Crear clase Libro.
2. Crear clase Celular.
3. Crear clase Película.
4. Crear clase Producto.
5. Crear clase Computadora.

---

## 🟡 Intermedios

6. Sistema de estudiantes.
7. Sistema de notas.
8. Sistema de biblioteca.
9. Sistema de inventario.
10. Sistema de empleados.

---

## 🔴 Avanzados

11. Sistema bancario.
12. Cajero automático.
13. Sistema de reservas.
14. Sistema hospitalario.
15. Sistema de ventas.

---

# 🧠 RETO FINAL

# Sistema de Tienda

Crear:

## Clase Producto

- nombre
- precio
- stock

## Clase Cliente

- nombre
- carrito

## Métodos

- agregar_producto()
- vender()
- mostrar_factura()

---

# 📌 Conceptos Aprendidos

✅ Clases  
✅ Objetos  
✅ Constructores  
✅ Métodos  
✅ Atributos  
✅ Encapsulamiento  
✅ Herencia  
✅ Polimorfismo  

---

# 🏠 Actividad para Casa

Crear un sistema orientado a objetos relacionado con:

- Universidad
- Hospital
- Restaurante
- Banco
- Videojuegos

Debe incluir:

✅ mínimo 3 clases  
✅ herencia  
✅ encapsulamiento  
✅ métodos  
✅ objetos funcionando  

---

# 🎓 Conclusión

La Programación Orientada a Objetos permite desarrollar aplicaciones más organizadas, reutilizables y fáciles de mantener.

Python facilita el aprendizaje de POO gracias a su sintaxis simple y clara.

