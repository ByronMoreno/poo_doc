# Clase: Herencia Múltiple en Python

## Carrera
Desarrollo de Software

## Asignatura
Progamación orienda a objetos

## Unidad
Herencia y Reutilización de Código

## Duración
3 horas académicas

---

# Objetivo de Aprendizaje

Al finalizar la clase, el estudiante será capaz de implementar herencia múltiple en Python para reutilizar funcionalidades de varias clases, comprendiendo su sintaxis, funcionamiento, ventajas, limitaciones y aplicaciones prácticas.

---

# Resultados de Aprendizaje

Los estudiantes podrán:

- Comprender el concepto de herencia múltiple.
- Diferenciar herencia simple y herencia múltiple.
- Crear clases que hereden de múltiples clases padre.
- Utilizar métodos y atributos heredados de varias clases.
- Comprender el orden de resolución de métodos (MRO).
- Resolver conflictos cuando existen métodos con el mismo nombre.

---

# Introducción

La herencia es uno de los pilares fundamentales de la Programación Orientada a Objetos.

Permite que una clase reutilice atributos y métodos definidos en otra clase.

Python soporta:

- Herencia Simple
- Herencia Multinivel
- Herencia Jerárquica
- Herencia Múltiple

---

# Repaso: Herencia Simple

## Ejemplo

```python
class Persona:

    def hablar(self):
        print("La persona puede hablar")


class Estudiante(Persona):
    pass


e1 = Estudiante()
e1.hablar()
```

### Resultado

```text
La persona puede hablar
```

---

# ¿Qué es la Herencia Múltiple?

La herencia múltiple ocurre cuando una clase hereda características de dos o más clases padre.

## Sintaxis

```python
class Hijo(Padre1, Padre2):
    pass
```

---

# Diagrama Conceptual

```text
        Padre1
           |
           |
        Padre2
           |
           |
         Hijo
```

Más correctamente:

```text
      Padre1      Padre2
          \        /
           \      /
             Hijo
```

---

# Ejemplo Básico

```python
class Caminar:

    def caminar(self):
        print("Estoy caminando")


class Hablar:

    def hablar(self):
        print("Estoy hablando")


class Persona(Caminar, Hablar):
    pass


p = Persona()

p.caminar()
p.hablar()
```

---

# Salida

```text
Estoy caminando
Estoy hablando
```

---

# Explicación

La clase Persona hereda:

- Método caminar() de Caminar
- Método hablar() de Hablar

Por lo tanto puede utilizar ambos métodos.

---

# Ejemplo 2: Empleado de una Empresa

## Clase Identificación

```python
class Identificacion:

    def mostrar_cedula(self):
        print("Cedula: 1723456789")
```

---

## Clase Contacto

```python
class Contacto:

    def mostrar_correo(self):
        print("Correo: empleado@empresa.com")
```

---

## Clase Empleado

```python
class Empleado(Identificacion, Contacto):
    pass
```

---

## Programa Completo

```python
class Identificacion:

    def mostrar_cedula(self):
        print("Cedula: 1723456789")


class Contacto:

    def mostrar_correo(self):
        print("Correo: empleado@empresa.com")


class Empleado(Identificacion, Contacto):
    pass


emp = Empleado()

emp.mostrar_cedula()
emp.mostrar_correo()
```

---

# Salida

```text
Cedula: 1723456789
Correo: empleado@empresa.com
```

---

# Constructor en Herencia Múltiple

## Clase Padre 1

```python
class Persona:

    def __init__(self):
        print("Constructor Persona")
```

---

## Clase Padre 2

```python
class Trabajador:

    def __init__(self):
        print("Constructor Trabajador")
```

---

## Clase Hija

```python
class Empleado(Persona, Trabajador):
    pass
```

---

## Prueba

```python
e = Empleado()
```

### Resultado

```text
Constructor Persona
```

---

# ¿Por qué sucede esto?

Python utiliza un mecanismo llamado:

## MRO (Method Resolution Order)

Determina qué método debe ejecutarse primero.

---

# Orden de Resolución

```python
class Empleado(Persona, Trabajador):
    pass
```

Python buscará en:

```text
1. Empleado
2. Persona
3. Trabajador
4. object
```

---

# Consultar el MRO

```python
print(Empleado.__mro__)
```

o

```python
print(Empleado.mro())
```

---

# Resultado

```text
Empleado
Persona
Trabajador
object
```

---

# Problema de Ambigüedad

Supongamos:

```python
class Padre1:

    def saludar(self):
        print("Hola desde Padre1")


class Padre2:

    def saludar(self):
        print("Hola desde Padre2")
```

---

# Clase Hija

```python
class Hijo(Padre1, Padre2):
    pass
```

---

# Prueba

```python
h = Hijo()
h.saludar()
```

---

# Resultado

```text
Hola desde Padre1
```

---

# Explicación

Python toma el método de la primera clase especificada.

```python
class Hijo(Padre1, Padre2)
```

Primero busca en Padre1.

---

# Cambiando el Orden

```python
class Hijo(Padre2, Padre1):
    pass
```

---

## Resultado

```text
Hola desde Padre2
```

---

# Uso de super()

El método super() permite acceder a métodos de las clases padre.

---

## Ejemplo

```python
class Persona:

    def saludar(self):
        print("Hola desde Persona")


class Estudiante(Persona):

    def saludar(self):
        super().saludar()
        print("Hola desde Estudiante")


e = Estudiante()
e.saludar()
```

---

# Resultado

```text
Hola desde Persona
Hola desde Estudiante
```

---

# Caso Práctico: Sistema Universitario

## Clase Estudiante

```python
class Estudiante:

    def estudiar(self):
        print("Estudiando...")
```

---

## Clase Deportista

```python
class Deportista:

    def entrenar(self):
        print("Entrenando...")
```

---

## Clase Universitario

```python
class Universitario(Estudiante, Deportista):
    pass
```

---

## Programa

```python
class Estudiante:

    def estudiar(self):
        print("Estudiando...")


class Deportista:

    def entrenar(self):
        print("Entrenando...")


class Universitario(Estudiante, Deportista):
    pass


u = Universitario()

u.estudiar()
u.entrenar()
```

---

# Salida

```text
Estudiando...
Entrenando...
```

---

# Ventajas de la Herencia Múltiple

✅ Reutilización de código.

✅ Menor duplicación.

✅ Diseño más flexible.

✅ Facilita la combinación de funcionalidades.

---

# Desventajas

❌ Puede generar ambigüedad.

❌ Hace más complejo el mantenimiento.

❌ Puede dificultar la comprensión del código.

❌ Problemas cuando varias clases tienen métodos iguales.

---

# Buenas Prácticas

✅ Utilizar herencia múltiple solo cuando sea necesaria.

✅ Mantener clases pequeñas y especializadas.

✅ Evitar cadenas de herencia demasiado largas.

✅ Comprender el MRO antes de implementar.

✅ Utilizar nombres claros para métodos y atributos.

---

# Ejercicio Guiado

Crear las siguientes clases:

## Clase Volador

```python
volar()
```

Mostrar:

```text
Puedo volar
```

---

## Clase Nadador

```python
nadar()
```

Mostrar:

```text
Puedo nadar
```

---

## Clase Pato

Debe heredar de:

```python
Volador
Nadador
```

---

## Resultado esperado

```text
Puedo volar
Puedo nadar
```

---

# Actividad Práctica

Desarrollar un sistema para un instituto tecnológico.

## Clase Persona

Método:

```python
presentarse()
```

---

## Clase Docente

Método:

```python
enseñar()
```

---

## Clase Investigador

Método:

```python
investigar()
```

---

## Clase DocenteInvestigador

Debe heredar de:

```python
Docente
Investigador
Persona
```

---

# Requisitos

El programa debe permitir:

1. Crear un objeto.
2. Ejecutar todos los métodos heredados.
3. Mostrar el MRO de la clase.
4. Explicar mediante comentarios cuál método se ejecuta primero.

---

# Resumen de la Clase

Conceptos aprendidos:

- Herencia múltiple.
- Sintaxis de herencia múltiple.
- Reutilización de código.
- Conflictos de métodos.
- Orden de resolución de métodos (MRO).
- Uso de super().
- Aplicaciones prácticas.

---

# Tarea

Desarrollar un sistema para una clínica.

## Clase Persona

Método:

```python
mostrar_nombre()
```

---

## Clase Médico

Método:

```python
atender_paciente()
```

---

## Clase Investigador

Método:

```python
realizar_estudio()
```

---

## Clase MédicoInvestigador

Debe heredar de Médico e Investigador.

### El programa debe:

- Crear un objeto.
- Utilizar todos los métodos heredados.
- Mostrar el MRO.
- Explicar mediante comentarios el funcionamiento de la herencia múltiple.