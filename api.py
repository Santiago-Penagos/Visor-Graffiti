from flask import Flask, jsonify, render_template  # Framework web
from backend import obtener_grafitis  # Logica de negocio en el backend

app = Flask(__name__)


@app.route("/api/grafitis")
def api_grafitis():
    """Endpoint: devuelve la lista de grafitis en JSON."""
    return jsonify(obtener_grafitis())


@app.route("/")
def index():
    """Sirve la pagina principal para evitar problemas de CORS."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
