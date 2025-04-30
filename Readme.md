# WSGI y ASGI en Python: Guía Práctica con Ejemplos

Este documento proporciona una guía práctica sobre el uso de WSGI y ASGI en Python, junto con ejemplos de implementación en frameworks populares como Flask, Starlette, Django y FastAPI.

## ¿Qué son WSGI y ASGI?

- **WSGI (Web Server Gateway Interface):** Es una interfaz estándar para la comunicación entre servidores web y aplicaciones web en Python. Define un protocolo simple para que el servidor web y la aplicación web puedan intercambiar información.
- **ASGI (Asynchronous Server Gateway Interface):** Es una extensión de WSGI que permite a las aplicaciones web Python utilizar características asíncronas, como la concurrencia, para mejorar el rendimiento y la escalabilidad.

## WSGI

WSGI es el estándar más antiguo y sigue siendo relevante para aplicaciones web más simples o aquellas que no necesitan las características asíncronas de ASGI.

### Ejemplo con Flask

Flask es un microframework web que utiliza WSGI.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola, mundo!"

if __name__ == "__main__":
    app.run(debug=True)
```

**Ejecución desde la terminal:**

```bash
python app.py
```

**O de la siguiente forma**

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

**Ejecución desde la terminal:**

```bash
flask --app app run --host=0.0.0.0 --debug --port=5002
```

## ASGI

ASGI es más moderno y adecuado para aplicaciones web que necesitan un alto rendimiento y escalabilidad.

### Ejemplo con Starlette

Starlette es un framework ASGI ligero que se basa en Starlette.

```python
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import HTMLResponse

app = Starlette([
    Route("/hello", HTMLResponse("¡Hola, mundo!"))
])

# Para ejecutarlo, necesitas un servidor ASGI como uvicorn
# uvicorn main:app --host 0.0.0.0 --port 8000
```

**Ejecución desde la terminal:**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

**O también puedes usar el siguiente código para ejecutarlo directamente:**

```python
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import HTMLResponse

app = Starlette(
    [
        Route("/hello", HTMLResponse("¡Hola, mundo!"))
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
```

### Ejemplo con Django

Django es un framework web completo que utiliza ASGI.

```python
from asgiref.sync import sync_to_async
from asgiref.utils import sync
from django.core import views
from django.urls import path
from django.conf import settings

# ... (Código de configuración de Django) ...

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]

# Para ejecutarlo, necesitas un servidor ASGI como uvicorn
# uvicorn main:app --host 0.0.0.0 --port 8000
```

**Ejecución desde la terminal:**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

**O también puedes usar el siguiente código para ejecutarlo directamente:**

```python
from django.core import handlers
from django.urls import path
from starlette.routing import StarletteRoute
from starlette.responses import HTMLResponse

def django_starlette_app(debug=True):
    app = Starlette(
        [
            StarletteRoute("/hello", HTMLResponse("¡Hola, mundo!"))
        ]
    )
    return app

if __name__ == "__main__":
    django_starlette_app()
```

### Ejemplo con FastAPI

FastAPI es un framework moderno y de alto rendimiento para construir APIs con Python, utilizando ASGI.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Hola, mundo!"}

# Para ejecutarlo, necesitas un servidor ASGI como uvicorn
# uvicorn main:app --host 0.0.0.0 --port 8000
```

**Ejecución desde la terminal:**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

**O también puedes usar el siguiente código para ejecutarlo directamente:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Hola, mundo!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

- **Flask:** Flask soporta WSGI de forma nativa. Puedes usar servidores WSGI como Gunicorn o uWSGI para desplegar aplicaciones Flask.
- **FastAPI:** FastAPI es un framework web moderno para construir APIs. Utiliza ASGI de forma nativa y es ideal para aplicaciones que requieren alto rendimiento.
- **Starlette:** Starlette es un framework ASGI que proporciona las bases para construir aplicaciones web asíncronas.
- **Django:** Django originalmente utilizaba WSGI, pero ahora también soporta ASGI a través de su servidor ASGI integrado y otros servidores ASGI.

## Consideraciones Finales

- **Rendimiento:** ASGI puede mejorar significativamente el rendimiento de las aplicaciones web Python, especialmente aquellas que realizan operaciones de E/S no bloqueantes.
- **Asincronía:** Utiliza las características asíncronas de Python (async/await) para aprovechar al máximo las ventajas de ASGI.
- **Servidores:** Elige un servidor ASGI que se adapte a tus necesidades. Algunos servidores populares incluyen Uvicorn, Hypercorn y Daphne.
