# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY pyproject.toml ./

RUN uv pip install --system "mcp[cli]>=1.6.0"

COPY main.py ./
COPY server.py ./

CMD ["uv", "run", "main.py"] 