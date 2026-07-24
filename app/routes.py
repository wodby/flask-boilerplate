import platform
from importlib.metadata import version

from flask import Blueprint, jsonify, render_template

routes = Blueprint("routes", __name__)


@routes.get("/")
def index():
    """Render the starter landing page."""
    return render_template(
        "index.html",
        flask_version=version("flask"),
        python_version=platform.python_version(),
    )


@routes.get("/api/status")
def status():
    """Demonstrate a JSON application response."""
    return jsonify(
        status="ok",
        runtime=f"Python {platform.python_version()}",
        framework=f"Flask {version('flask')}",
    )


@routes.get("/healthz")
def healthz():
    """Report that the application can serve requests."""
    return jsonify(status="ok")
