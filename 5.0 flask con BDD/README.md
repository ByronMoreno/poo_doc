# Clase: Conectando Flask con PostgreSQL

## Objetivos

Al finalizar la clase los estudiantes podrán:

- Instalar las dependencias necesarias.
- Conectar Flask con PostgreSQL.
- Consultar datos desde una tabla.
- Mostrar los resultados en una página web.
- Comprender el flujo básico entre Flask, PostgreSQL y HTML.

---

# 1. Crear el entorno virtual

```bash
python -m venv venv
```

Activar en Windows:

```bash
venv\Scripts\activate
```

---

# 2. Instalar dependencias

```bash
pip install flask psycopg2-binary
```

Verificar:

```bash
pip list
```

---

# 3. Crear una base de datos

```sql
CREATE DATABASE escuela;
```

Conectarse a la base:

```sql
\c escuela
```

Crear tabla:

```sql
CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT
);
```

Insertar datos:

```sql
INSERT INTO estudiantes(nombre, edad)
VALUES
('Juan', 20),
('María', 22),
('Pedro', 19);
```

---

# 4. Estructura del proyecto

```text
mi_proyecto/
│
├── app.py
└── templates/
    └── estudiantes.html
```

---

# 5. Conexión a PostgreSQL

Archivo `app.py`

```python
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def obtener_conexion():
    return psycopg2.connect(
        host="localhost",
        database="escuela",
        user="postgres",
        password="1234"
    )
```

---

# 6. Crear una ruta que consulte datos

```python
@app.route("/")
def inicio():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM estudiantes")

    estudiantes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "estudiantes.html",
        estudiantes=estudiantes
    )

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 7. Crear la vista HTML

Archivo `templates/estudiantes.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Estudiantes</title>
</head>
<body>

    <h1>Lista de estudiantes</h1>

    <table border="1">
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Edad</th>
        </tr>

        {% for estudiante in estudiantes %}
        <tr>
            <td>{{ estudiante[0] }}</td>
            <td>{{ estudiante[1] }}</td>
            <td>{{ estudiante[2] }}</td>
        </tr>
        {% endfor %}

    </table>

</body>
</html>
```

---

# 8. Ejecutar la aplicación

```bash
python app.py
```

Abrir:

```text
http://localhost:5000
```

Deberían ver la lista de estudiantes obtenida desde PostgreSQL.

---

# Ejercicio para los estudiantes

Crear una tabla llamada `productos`.

```sql
CREATE TABLE productos(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio NUMERIC(10,2)
);
```

Insertar al menos 5 productos.

Luego:

1. Crear una ruta `/productos`.
2. Consultar los productos desde PostgreSQL.
3. Mostrar los resultados en una tabla HTML.

---

# Resumen

En esta clase aprendimos a:

- Crear una base de datos PostgreSQL.
- Crear tablas e insertar registros.
- Conectar Flask con PostgreSQL usando `psycopg2`.
- Ejecutar consultas SQL desde Python.
- Mostrar información de la base de datos en una página HTML.

---

# Próxima Clase

## Formularios y CRUD con Flask

Temas:

- Formularios HTML.
- Métodos GET y POST.
- Insertar registros en PostgreSQL.
- Actualizar registros.
- Eliminar registros.
- Construcción de un CRUD completo.
