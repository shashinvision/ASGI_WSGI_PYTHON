# WSGI y ASGI en Python: Guía Práctica con Ejemplos

Este documento incluye una guía práctica sobre el uso de WSGI y ASGI en Python, con ejemplos funcionales en frameworks populares como Flask, Starlette, Django y FastAPI.

## ¿Qué son WSGI y ASGI?

- **WSGI (Web Server Gateway Interface):** Es una interfaz estándar para la comunicación entre servidores web y aplicaciones web en Python. Define un protocolo simple para el intercambio de información entre ambos.
- **ASGI (Asynchronous Server Gateway Interface):** Es una extensión moderna de WSGI que permite el uso de características asíncronas (como `async/await`) para mejorar el rendimiento y la escalabilidad.

---

## WSGI

WSGI es el estándar más antiguo, ideal para aplicaciones web más simples o que no requieren asincronía.

### Ejemplo con Flask (WSGI)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola, mundo!"

if __name__ == "__main__":
    app.run(debug=True)
```

**Ejecutar en terminal:**

```bash
python app.py
```

### Ejemplo más completo con Flask

```python
from flask import Flask, render_template, url_for, request
from language import english, spanish, generals
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/<language>", methods=["GET"])
def index(language="spanish"):
    if request.method == "GET":
        icon = url_for("static", filename="imgs/perfil.ico")
        current_year = datetime.now().year
        set_language = spanish if language == "spanish" else english

        return render_template(
            "index.html",
            icon=icon,
            language=set_language,
            generals=generals,
            current_year=current_year,
        )
    return "Invalid request method", 400
```

**Ejecutar en terminal:**

```bash
flask --app app run --host=0.0.0.0 --debug --port=5002
```

### Flask usando Waitress (servidor WSGI)

```python
from waitress import serve
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola desde Flask con Waitress!"

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)

```

**Ejecutar en terminal:**

```bash
python app.py
```

**O también:**

````bash

```python
from waitress import serve
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola desde Flask con Waitress!"


````

**Ejecutar en terminal:**

```bash
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

---

## ASGI

ASGI es el estándar moderno para aplicaciones que requieren alto rendimiento, asincronía y concurrencia.

### Ejemplo con Starlette

```python
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import HTMLResponse

async def hello(request):
    return HTMLResponse("\u00a1Hola, mundo!")

app = Starlette(
    routes=[
        Route("/hello", hello)
    ]
)
```

**Ejecutar con uvicorn:**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Ejemplo con Django (ASGI desde v3.0)

Django ofrece soporte ASGI a partir de la versión 3.0 a través del archivo `asgi.py`.

**Ejecutar con Daphne o Uvicorn:**

```bash
# Con Daphne
pip install daphne

daphne myproject.asgi:application

# O con uvicorn
uvicorn myproject.asgi:application --host 0.0.0.0 --port 8000
```

### Ejemplo con FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Hola, mundo!"}
```

**Ejecutar con uvicorn:**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

O bien:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## Comparación entre Frameworks

- **Flask:** Nativamente usa WSGI. Puedes desplegarlo con Gunicorn, uWSGI o Waitress.
- **FastAPI:** Usa ASGI de forma nativa. Ideal para APIs modernas y de alto rendimiento.
- **Starlette:** Framework ASGI minimalista y flexible.
- **Django:** Clásico framework WSGI, ahora compatible también con ASGI (desde v3.0).

---

## Consideraciones Finales

- **Rendimiento:** ASGI ofrece mejor rendimiento en tareas de E/S no bloqueantes.
- **Asincronía:** Utiliza `async/await` para sacar provecho de ASGI.
- **Compatibilidad:** Para aplicaciones simples, WSGI sigue siendo una buena opción.
- **Servidores ASGI populares:** Uvicorn, Daphne, Hypercorn.
- **Migración:** Cambiar de WSGI a ASGI puede requerir ajustes en configuraciones, middlewares y vistas.

---

Con esta guía tienes una base sólida para comprender y usar WSGI y ASGI según tus necesidades.
