# Clase: CRUD con Flask y PostgreSQL en un solo archivo

## Objetivo de la clase

Al finalizar esta práctica, el estudiante será capaz de:

- Conectar Flask con PostgreSQL.
- Crear una API REST que devuelva JSON.
- Realizar operaciones CRUD:
  - Crear (Create)
  - Consultar (Read)
  - Actualizar (Update)
  - Eliminar (Delete)
- Utilizar SQL desde Python mediante psycopg2.

---

# Requisitos

```bash
pip install flask psycopg2-binary
```

---

# Crear la Base de Datos

```sql
CREATE DATABASE curso_flask;
```

```sql
\c curso_flask
```

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
```

```sql
INSERT INTO usuarios(nombre)
VALUES
('Juan'),
('Maria');
```

---

# Estructura del Proyecto

```text
crud_flask_postgres/
│
├── app.py
└── requirements.txt
```

---

# Código Completo (app.py)

```python
from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

conexion = psycopg2.connect(
    host="localhost",
    database="curso_flask",
    user="postgres",
    password="123456",
    port="5432"
)

print("Conexión exitosa")

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, nombre FROM usuarios"
    )

    datos = cursor.fetchall()

    usuarios = []

    for usuario in datos:
        usuarios.append({
            "id": usuario[0],
            "nombre": usuario[1]
        })

    cursor.close()

    return jsonify(usuarios)


@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, nombre FROM usuarios WHERE id=%s",
        (id,)
    )

    usuario = cursor.fetchone()

    cursor.close()

    if usuario:
        return jsonify({
            "id": usuario[0],
            "nombre": usuario[1]
        })

    return jsonify({
        "error": "Usuario no encontrado"
    }), 404


@app.route('/usuarios', methods=['POST'])
def crear_usuario():

    datos = request.get_json()

    cursor = conexion.cursor()

    cursor.execute(
        'INSERT INTO usuarios(nombre) VALUES(%s) RETURNING id',
        (datos['nombre'],)
    )

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()

    return jsonify({
        'id': nuevo_id,
        'nombre': datos['nombre']
    }), 201


@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):

    datos = request.get_json()

    cursor = conexion.cursor()

    cursor.execute(
        'UPDATE usuarios SET nombre=%s WHERE id=%s',
        (datos['nombre'], id)
    )

    conexion.commit()

    cursor.close()

    return jsonify({
        'mensaje': 'Usuario actualizado correctamente'
    })


@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):

    cursor = conexion.cursor()

    cursor.execute(
        'DELETE FROM usuarios WHERE id=%s',
        (id,)
    )

    conexion.commit()

    cursor.close()

    return jsonify({
        'mensaje': 'Usuario eliminado correctamente'
    })


if __name__ == '__main__':
    app.run(debug=True)
```

---

# Ejecutar

```bash
python app.py
```

Servidor:

```text
http://127.0.0.1:5000
```

---

# Endpoints

## Obtener todos

```http
GET /usuarios
```

## Obtener uno

```http
GET /usuarios/1
```

## Crear

```http
POST /usuarios
```

```json
{
    "nombre": "Carlos"
}
```

## Actualizar

```http
PUT /usuarios/1
```

```json
{
    "nombre": "Pedro"
}
```

## Eliminar

```http
DELETE /usuarios/1
```

---

# Conceptos Aprendidos

- Flask
- PostgreSQL
- psycopg2
- API REST
- JSON
- CRUD
- SELECT
- INSERT
- UPDATE
- DELETE

---

# Ejercicio

Crear una tabla productos:

```sql
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio NUMERIC(10,2)
);
```

Implementar:

- GET /productos
- GET /productos/{id}
- POST /productos
- PUT /productos/{id}
- DELETE /productos/{id}

Resultado esperado:

```json
{
    "id": 1,
    "nombre": "Laptop",
    "precio": 1200.50
}
```

# Configuración Inicial de Git

## 1. Verificar que Git esté instalado

Abre **Git Bash** o una terminal y ejecuta:

```bash
git --version
```

Salida esperada:

```bash
git version 2.x.x
```

---

## 2. Configurar el nombre de usuario

Este nombre aparecerá en los commits realizados.

```bash
git config --global user.name "Byron Moreno"
```

Verificar la configuración:

```bash
git config --global user.name
```

---

## 3. Configurar el correo electrónico

Utiliza el correo asociado a tu cuenta de GitHub, GitLab o la plataforma que utilices.

```bash
git config --global user.email "correo@ejemplo.com"
```

Verificar la configuración:

```bash
git config --global user.email
```

---

## 4. Verificar toda la configuración

Mostrar todas las configuraciones globales de Git:

```bash
git config --list
```

También puedes consultar configuraciones específicas:

```bash
git config --global user.name
git config --global user.email
```