import os

from flask import Flask, jsonify
from werkzeug.exceptions import MethodNotAllowed
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app(test_config: dict | None = None) -> Flask:
    """Create and configure an isolated Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        TRUST_PROXY_HEADERS=os.environ.get("TRUST_PROXY_HEADERS", "true").lower()
        in {"1", "true", "yes"}
    )

    if test_config is not None:
        app.config.from_mapping(test_config)

    if app.config["TRUST_PROXY_HEADERS"]:
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

    from .routes import routes

    app.register_blueprint(routes)
    app.register_error_handler(404, not_found)
    app.register_error_handler(405, method_not_allowed)
    return app


def not_found(_error):
    """Return a consistent response for unknown routes."""
    return jsonify(detail="Not found"), 404


def method_not_allowed(error: MethodNotAllowed):
    """Preserve Flask's allowed methods in a JSON error response."""
    response = jsonify(detail="Method not allowed")
    response.status_code = 405
    if error.valid_methods:
        response.headers["Allow"] = ", ".join(error.valid_methods)
    return response


app = create_app()
