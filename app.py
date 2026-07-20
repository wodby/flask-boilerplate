from flask import Flask, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)


@app.get("/")
def index():
    return jsonify(message="Hello from Wodby Flask")


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")
