# Flask starter for Wodby

A production-oriented application for the [Wodby Flask service](https://github.com/wodby/service-flask) and [Flask stack](https://github.com/wodby/stack-flask).

It demonstrates:

- an application factory and blueprint-based route organization
- Jinja rendering and static assets
- JSON, health, not-found, and method-not-allowed responses
- explicit reverse-proxy handling for Wodby's route gateway
- pytest, Ruff, Gunicorn, and Wodby CI

## Local development

```shell
uv sync
uv run pytest
uv run flask --app app run --debug
```

Open <http://localhost:5000>. Useful endpoints are:

- `/` — the Jinja landing page
- `/api/status` — a JSON response example
- `/healthz` — the deployment health endpoint

## Project structure

- `app/__init__.py` owns application construction and middleware.
- `app/routes.py` contains the starter blueprint.
- `app/templates/` and `app/static/` demonstrate Flask's web resources.
- `tests/` creates isolated applications through the factory.

Wodby places one trusted route proxy in front of the application, so
`TRUST_PROXY_HEADERS` defaults to `true`. Set it to `false` when exposing
Gunicorn directly or when another component already normalizes forwarded
headers.

PostgreSQL, Valkey, and SMTP links are optional. When enabled, their connection
values are supplied through Wodby's documented environment variables.
