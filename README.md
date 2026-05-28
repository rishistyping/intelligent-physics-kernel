# Intelligent Physics Kernel

Interactive Marimo notebook for the Intelligent Physics Kernel / Intelligent Physics monograph. It presents the MU principle, the 10-lock derivation, E8 and H4 lattice visualizations, Spin(10) / Standard Model structure, the long-paper Table of Law, scorecard, derivation forest, falsification dashboard, traceability sheets, and deployment-ready public exports.

## Quick Start

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
make run
```

Open `http://localhost:2718`.

For the Marimo editor:

```bash
make edit
```

## Verify

```bash
make verify
```

This runs Python syntax checks, `marimo check`, static HTML export, Jupyter `.ipynb` export, a headless editor health check, and the local LaunchAgent health check when available.

For a fast CI/public-share gate only:

```bash
make verify-share
```

## Publish A Static Site

The fastest way to share publicly is a static Marimo export:

```bash
make site
make serve-site
```

Smoke-test `http://localhost:8000`, then publish the generated `site/` directory. The included GitHub Actions workflow at `.github/workflows/pages-static.yml` builds and deploys this static export to GitHub Pages when Pages is configured to use GitHub Actions.

Static export is best for broad public reading. It preserves the rendered visual narrative, but it is a snapshot: controls that need Python recomputation require the live Marimo app. The exported HTML also loads Marimo/runtime assets and fonts from public CDNs, so use a CDN-friendly CSP.

## Full Live Deployment

For the highest-fidelity public app, run the Python-backed Marimo server behind HTTPS and authentication:

```bash
docker build -t intelligent-physics-kernel:latest .
docker run --rm -p 127.0.0.1:2718:2718 intelligent-physics-kernel:latest
```

The Docker command binds to localhost for trusted reverse-proxy ingress. Do not expose the container directly to the public internet without auth/TLS. For public hosting, set Marimo auth at the platform/proxy layer or with Marimo's token-password environment support.

## Project Files

- `app.py` - primary Marimo notebook.
- `ipk_head.html` - II Logos theme, motion, cursor, and transition runtime.
- `DEPLOYMENT.md` - local LaunchAgent, public hosting, VS Code, and JupyterHub notes.
- `verify_editor_deployment.py` - repeatable local verification.
- `site/index.html` - generated static artifact after `make site`.
