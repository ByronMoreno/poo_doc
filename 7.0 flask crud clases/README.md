# 📌 API Flask + PostgreSQL (2 clases + explicación de `execute()`)

Este proyecto muestra una API REST simple utilizando Flask y PostgreSQL con una arquitectura mínima compuesta por únicamente dos archivos:

- `db.py`: conexión y ejecución de consultas SQL.
- `app.py`: API REST y lógica de negocio.

---

# 📁 Estructura del Proyecto

```text
cliente_api/
├── db.py
└── app.py
```

---

# 🗄️ Base de Datos

## Crear la Base de Datos

```sql
CREATE DATABASE clientes_db;
```

## Crear la Tabla

```sql
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(100)
);
```

---

# 📦 Instalación

## Instalar dependencias

```bash
pip install flask psycopg2
```

---

# 🔌 Archivo db.py

```python
import psycopg2

class Database:

    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="clientes_db",
            user="postgres",
            password="1234",
            port=5432
        )

    def execute(self, sql, params=None):
        """
        Ejecuta consultas SQL:
        SELECT, INSERT, UPDATE y DELETE
        """

        cursor = self.conn.cursor()

        cursor.execute(sql, params or ())

        if sql.strip().lower().startswith("select"):
            result = cursor.fetchall()
        else:
            self.conn.commit()
            result = None

        cursor.close()

        return result

    def close(self):
        self.conn.close()
```

---

# 🌐 Archivo app.py

```python
from flask import Flask, jsonify, request
from db import Database

app = Flask(__name__)

# ==========================
# LISTAR CLIENTES
# ==========================
@app.route("/clientes", methods=["GET"])
def listar_clientes():

    db = Database()

    data = db.execute(
        "SELECT id, nombre, apellido, email FROM cliente"
    )

    db.close()

    return jsonify(data)


# ==========================
# OBTENER CLIENTE POR ID
# ==========================
@app.route("/clientes/<int:id>", methods=["GET"])
def obtener_cliente(id):

    db = Database()

    data = db.execute(
        "SELECT id, nombre, apellido, email FROM cliente WHERE id=%s",
        (id,)
    )

    db.close()

    return jsonify(data)


# ==========================
# CREAR CLIENTE
# ==========================
@app.route("/clientes", methods=["POST"])
def crear_cliente():

    data = request.json

    db = Database()

    db.execute(
        """
        INSERT INTO cliente(nombre, apellido, email)
        VALUES (%s, %s, %s)
        """,
        (
            data["nombre"],
            data["apellido"],
            data["email"]
        )
    )

    db.close()

    return jsonify({
        "mensaje": "Cliente creado"
    }), 201


# ==========================
# ACTUALIZAR CLIENTE
# ==========================
@app.route("/clientes/<int:id>", methods=["PUT"])
def actualizar_cliente(id):

    data = request.json

    db = Database()

    db.execute(
        """
        UPDATE cliente
        SET nombre=%s,
            apellido=%s,
            email=%s
        WHERE id=%s
        """,
        (
            data["nombre"],
            data["apellido"],
            data["email"],
            id
        )
    )

    db.close()

    return jsonify({
        "mensaje": "Cliente actualizado"
    })


# ==========================
# ELIMINAR CLIENTE
# ==========================
@app.route("/clientes/<int:id>", methods=["DELETE"])
def eliminar_cliente(id):

    db = Database()

    db.execute(
        "DELETE FROM cliente WHERE id=%s",
        (id,)
    )

    db.close()

    return jsonify({
        "mensaje": "Cliente eliminado"
    })


# ==========================
# INICIAR APLICACIÓN
# ==========================
if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🧠 Explicación del Método `execute()`

Este método centraliza la ejecución de todas las consultas SQL de la aplicación.

```python
def execute(self, sql, params=None):
```

### Parámetros

| Parámetro | Descripción |
|------------|------------|
| sql | Consulta SQL a ejecutar |
| params | Valores para reemplazar los `%s` |

---

## Paso 1: Crear un cursor

```python
cursor = self.conn.cursor()
```

El cursor es el objeto encargado de comunicarse con PostgreSQL.

---

## Paso 2: Ejecutar la consulta

```python
cursor.execute(sql, params or ())
```

Ejemplo:

```python
cursor.execute(
    "SELECT * FROM cliente WHERE id=%s",
    (1,)
)
```

---

## Paso 3: Detectar si es un SELECT

```python
if sql.strip().lower().startswith("select"):
```

La función:

- elimina espacios con `strip()`
- convierte a minúsculas con `lower()`
- verifica si inicia con `"select"`

---

## Paso 4: Obtener resultados

```python
result = cursor.fetchall()
```

Devuelve todos los registros encontrados.

Ejemplo:

```python
[
    (1, 'Juan', 'Perez', 'juan@mail.com'),
    (2, 'Ana', 'Lopez', 'ana@mail.com')
]
```

---

## Paso 5: Guardar cambios

Si la consulta no es SELECT:

```python
self.conn.commit()
```

Esto aplica para:

- INSERT
- UPDATE
- DELETE

---

## Paso 6: Cerrar el cursor

```python
cursor.close()
```

Libera memoria y recursos de la conexión.

---

## Paso 7: Retornar el resultado

```python
return result
```

### Resultado según el tipo de consulta

| Consulta | Retorno |
|-----------|---------|
| SELECT | Lista de registros |
| INSERT | None |
| UPDATE | None |
| DELETE | None |

---

# 🧪 Ejemplos de Uso

## SELECT

```python
db = Database()

clientes = db.execute(
    "SELECT * FROM cliente"
)

db.close()

print(clientes)
```

Salida:

```python
[
    (1, 'Juan', 'Perez', 'juan@mail.com')
]
```

---

## INSERT

```python
db = Database()

db.execute(
    """
    INSERT INTO cliente(nombre, apellido, email)
    VALUES (%s, %s, %s)
    """,
    (
        "Ana",
        "Lopez",
        "ana@mail.com"
    )
)

db.close()
```

---

## UPDATE

```python
db.execute(
    """
    UPDATE cliente
    SET email=%s
    WHERE id=%s
    """,
    (
        "nuevo@mail.com",
        1
    )
)
```

---

## DELETE

```python
db.execute(
    "DELETE FROM cliente WHERE id=%s",
    (1,)
)
```

---

# 🚀 Ventajas de este Diseño

- Solo 2 archivos.
- Fácil de enseñar a estudiantes.
- Código sencillo y entendible.
- Separación básica entre conexión y API.
- Fácil de migrar a arquitecturas más avanzadas.
- Base ideal para evolucionar a:
  - Repository Pattern
  - Service Layer
  - JWT
  - Docker
  - Microservicios
  - Arquitectura estilo Spring Boot

---

# 🔮 Posibles Mejoras

- Manejo de excepciones con `try/except`.
- Uso de `fetchone()` para consultas por ID.
- Pool de conexiones.
- Variables de entorno para credenciales.
- Validaciones de entrada.
- Logging.
- Swagger/OpenAPI.
- JWT Authentication.
- Docker y Docker Compose.
- Arquitectura Controller-Service-Repository.