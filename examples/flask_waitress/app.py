from waitress import serve
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "¡Hola desde Flask con Waitress!"


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5012)
