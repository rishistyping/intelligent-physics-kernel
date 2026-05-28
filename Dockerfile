FROM python:3.11.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN useradd --create-home --shell /usr/sbin/nologin marimo \
    && chown -R marimo:marimo /app

USER marimo

EXPOSE 2718

# Health endpoints (automatically provided by marimo):
#   /health
#   /healthz
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:2718/health', timeout=3).read()" || exit 1

# Run as a read-only app for local Docker or trusted ingress.
# Public hosting should put this behind TLS/auth or set MARIMO_TOKEN_PASSWORD.
# Add --include-code if you want viewers to see the source.
CMD ["marimo", "run", "app.py", "--headless", "--host", "0.0.0.0", "--port", "2718"]
