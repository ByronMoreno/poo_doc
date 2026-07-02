# CRUD Flask + PostgreSQL + Jinja2

## Estructura

``` text
crud_flask/
│── app.py
│── database.py
│── requirements.txt
│── schema.sql
└── templates/
    │── index.html
    └── editar.html
```

## schema.sql

``` sql
CREATE DATABASE inventario;

\c inventario

CREATE TABLE productos(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL
);
```

## requirements.txt

``` text
Flask
psycopg2-binary
```

Instalar:

``` bash
pip install -r requirements.txt
```

## database.py

``` python
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="inventario",
        user="postgres",
        password="123456"
    )
```

## app.py

``` python
from flask import Flask, render_template, request, redirect
from database import get_connection

app = Flask(__name__)

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY id")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", productos=productos)

@app.route("/guardar", methods=["POST"])
def guardar():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos(nombre,precio) VALUES(%s,%s)",
        (nombre, precio)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

@app.route("/editar/<int:id>")
def editar(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id=%s",(id,))
    producto = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("editar.html", producto=producto)

@app.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE productos SET nombre=%s, precio=%s WHERE id=%s",
        (nombre, precio, id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id=%s",(id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
```

## templates/index.html

``` html
<!DOCTYPE html>
<html>
<head>
    <title>CRUD Productos</title>
</head>
<body>

<h2>Nuevo Producto</h2>

<form action="/guardar" method="POST">
    <input type="text" name="nombre" placeholder="Nombre" required>
    <input type="number" step="0.01" name="precio" placeholder="Precio" required>
    <button>Guardar</button>
</form>

<hr>

<h2>Lista de Productos</h2>

<table border="1">
<tr>
    <th>ID</th>
    <th>Nombre</th>
    <th>Precio</th>
    <th>Acciones</th>
</tr>

{% for producto in productos %}
<tr>
    <td>{{ producto[0] }}</td>
    <td>{{ producto[1] }}</td>
    <td>{{ producto[2] }}</td>
    <td>
        <a href="/editar/{{ producto[0] }}">Editar</a> |
        <a href="/eliminar/{{ producto[0] }}">Eliminar</a>
    </td>
</tr>
{% endfor %}

</table>

</body>
</html>
```

## templates/editar.html

``` html
<!DOCTYPE html>
<html>
<head>
    <title>Editar Producto</title>
</head>
<body>

<h2>Editar Producto</h2>

<form action="/actualizar/{{ producto[0] }}" method="POST">
    <input type="text" name="nombre" value="{{ producto[1] }}" required>
    <input type="number" step="0.01" name="precio" value="{{ producto[2] }}" required>
    <button>Actualizar</button>
</form>

<br>
<a href="/">Regresar</a>

</body>
</html>
```

## Ejecutar

``` bash
python app.py
```

Abrir:

    http://localhost:5000
