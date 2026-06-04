# Clase: Introducción al Desarrollo Web con Flask

## Carrera
Desarrollo de Software

## Asignatura
Programación orientada a objetos

## Unidad
Desarrollo de Aplicaciones Web con Flask

## Duración
3 horas académicas

---

# Objetivo de Aprendizaje

Al finalizar la clase, el estudiante será capaz de desarrollar una aplicación web básica utilizando Flask, comprendiendo la arquitectura cliente-servidor, la creación de rutas y la generación de respuestas HTTP mediante la construcción de un proyecto "Hola Mundo".

---

# Resultados de Aprendizaje

Los estudiantes podrán:

- Explicar qué es Flask y sus principales características.
- Comprender el funcionamiento de una aplicación web basada en Python.
- Instalar y configurar Flask en un entorno de desarrollo.
- Crear una aplicación web básica.
- Definir rutas utilizando decoradores.
- Ejecutar un servidor web local.
- Probar una aplicación Flask desde un navegador web.

---

# 1. Introducción al Desarrollo Web

## ¿Qué es una Aplicación Web?

Una aplicación web es un software que se ejecuta en un servidor y es accesible mediante un navegador web.

### Ejemplos

- Gmail
- Facebook
- Moodle
- Sistemas Académicos
- Sistemas Bancarios

---

## Arquitectura Cliente - Servidor

```text
+-------------+      HTTP      +-------------+
| Navegador   | <-----------> | Servidor    |
| (Cliente)   |               | Flask       |
+-------------+               +-------------+
```

### Cliente

Es quien realiza la petición.

Ejemplos:

- Chrome
- Firefox
- Edge

### Servidor

Es quien procesa la solicitud y devuelve una respuesta.

Ejemplos:

- Flask
- Django
- Spring Boot
- Node.js

---

# 2. ¿Qué es Flask?

Flask es un microframework para Python que permite desarrollar aplicaciones web de forma rápida y sencilla.

Fue creado por:

**Armin Ronacher**

---

## Características de Flask

✅ Ligero

✅ Fácil de aprender

✅ Flexible

✅ Basado en Python

✅ Ideal para APIs REST

✅ Muy utilizado en microservicios

---

## Flask vs Django

| Característica | Flask | Django |
|---------------|--------|---------|
| Tamaño | Pequeño | Grande |
| Curva de aprendizaje | Baja | Media |
| Flexibilidad | Alta | Media |
| Velocidad de desarrollo | Rápida | Muy rápida |
| Ideal para | APIs y Microservicios | Aplicaciones completas |

---

# 3. Instalación de Flask

## Verificar Python

```bash
python --version
```

o

```bash
python3 --version
```

Resultado esperado:

```bash
Python 3.13.0
```

---

## Crear un entorno virtual

Windows

```bash
python -m venv venv
```

Linux

```bash
python3 -m venv venv
```

---

## Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux

```bash
source venv/bin/activate
```

---

## Instalar Flask

```bash
pip install flask
```

Verificar instalación:

```bash
pip list
```

Resultado esperado:

```text
Flask
Werkzeug
Jinja2
Click
```

---

# 4. Primer Proyecto Flask

## Estructura Inicial

```text
flask_hola_mundo/
│
├── app.py
│
└── venv/
```

---

# 5. Hola Mundo en Flask

## Archivo app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Hola Mundo desde Flask"

if __name__ == '__main__':
    app.run(debug=True)
```

---

# Explicación del Código

## Importación

```python
from flask import Flask
```

Importa la clase principal de Flask.

---

## Crear la aplicación

```python
app = Flask(__name__)
```

Crea una instancia de la aplicación.

---

## Crear una ruta

```python
@app.route('/')
```

Indica que la función responderá cuando el usuario visite:

```text
http://localhost:5000
```

---

## Función asociada

```python
def inicio():
    return "Hola Mundo desde Flask"
```

Devuelve una respuesta al navegador.

---

## Iniciar servidor

```python
app.run(debug=True)
```

Levanta el servidor web.

---

# 6. Ejecutar la Aplicación

Desde la terminal:

```bash
python app.py
```

Resultado:

```text
* Running on http://127.0.0.1:5000
```

Abrir en el navegador:

```text
http://localhost:5000
```

Visualización:

```text
Hola Mundo desde Flask
```

---

# 7. Creando Más Rutas

Modificar:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Página Principal"

@app.route('/acerca')
def acerca():
    return "Acerca de Nosotros"

@app.route('/contacto')
def contacto():
    return "Página de Contacto"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Pruebas

### Inicio

```text
http://localhost:5000
```

### Acerca

```text
http://localhost:5000/acerca
```

### Contacto

```text
http://localhost:5000/contacto
```

---

# 8. Parámetros en la URL

```python
from flask import Flask

app = Flask(__name__)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"Hola {nombre}"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Ejemplo

URL:

```text
http://localhost:5000/saludo/Byron
```

Resultado:

```text
Hola Byron
```

---

# 9. Modo Debug

```python
app.run(debug=True)
```

Permite:

- Recarga automática.
- Visualización de errores.
- Mayor velocidad de desarrollo.

---

## Ventajas

```text
Guardar archivo
       ↓
Flask detecta cambios
       ↓
Reinicia automáticamente
```

---

# 10. Flujo de una Petición Flask

```text
Usuario
   │
   ▼
Navegador
   │
   ▼
URL
   │
   ▼
Flask
   │
   ▼
Ruta
   │
   ▼
Función
   │
   ▼
Respuesta
   │
   ▼
Navegador
```

---

# Ejercicio Guiado

## Crear las siguientes rutas

```text
/
```

Mostrar:

```text
Bienvenidos al curso de Flask
```

---

```text
/estudiante
```

Mostrar:

```text
Nombre del estudiante
```

---

```text
/docente
```

Mostrar:

```text
Nombre del docente
```

---

```text
/materia
```

Mostrar:

```text
Programación con Python
```

---

# Actividad Práctica

Desarrollar una aplicación Flask para una institución educativa.

Debe contener:

## Ruta principal

```text
/
```

Mensaje de bienvenida.

---

## Ruta carrera

```text
/carrera
```

Mostrar el nombre de la carrera.

---

## Ruta profesor

```text
/profesor
```

Mostrar el nombre del docente.

---

## Ruta estudiante

```text
/estudiante/<nombre>
```

Mostrar:

```text
Bienvenido Nombre
```

---

# Buenas Prácticas

✅ Utilizar nombres descriptivos.

✅ Mantener el código organizado.

✅ Usar entorno virtual.

✅ Comentar cuando sea necesario.

✅ Probar cada ruta antes de continuar.

---

# Resumen de la Clase

Flask permite desarrollar aplicaciones web utilizando Python de manera sencilla.

Conceptos aprendidos:

- Arquitectura Cliente-Servidor.
- Framework Flask.
- Instalación de Flask.
- Aplicación Hola Mundo.
- Rutas.
- Decoradores.
- Parámetros en URL.
- Ejecución de servidor local.
- Modo Debug.

---

# Tarea

Investigar y presentar:

1. ¿Qué es HTTP?
2. ¿Qué es una petición GET?
3. ¿Qué es una petición POST?
4. ¿Qué es una API REST?
5. Diferencias entre Flask y Django.

Además, desarrollar una aplicación Flask con al menos 5 rutas diferentes y capturas de pantalla de su funcionamiento.