# Minimal Flask boilerplate

Minimal application for the [Wodby Flask service](https://github.com/wodby/service-flask) and [Flask stack](https://github.com/wodby/stack-flask).

The project uses [uv](https://docs.astral.sh/uv/) and includes a Wodby CI pipeline.

## Local development

```shell
uv sync
uv run pytest
uv run flask --app app run --debug
```

Open http://localhost:5000. A health endpoint is available at `/healthz`.
