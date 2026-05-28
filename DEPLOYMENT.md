# Deployment Guide

This project has two publish lanes:

1. **Static public snapshot** - fastest and safest for sharing. It exports the rendered Marimo notebook to `site/index.html` and can be hosted on GitHub Pages, Cloudflare Pages, Netlify, Vercel static hosting, or any static web server.
2. **Live Marimo app** - highest fidelity. It keeps Python-backed controls live, but must sit behind HTTPS and authentication.

## Fast Public Share

```bash
make site
make verify-share
make serve-site
```

Open `http://localhost:8000` and smoke-test the page. Then publish the generated `site/` directory.

Important static-export behavior:

- Static HTML is a snapshot of the notebook outputs. Controls that require Python recomputation need the live app.
- The exported page loads Marimo/runtime assets and fonts from public CDNs, so host it with a CDN-friendly content-security policy.
- `site/.nojekyll` is required for GitHub Pages.

## GitHub Pages

The repository includes `.github/workflows/pages-static.yml`. After pushing to GitHub:

1. Open repository **Settings -> Pages**.
2. Set **Build and deployment -> Source** to **GitHub Actions**.
3. Push to `main` or run the workflow manually.

The workflow installs pinned Python dependencies, compiles `app.py` and the verifier, runs `marimo check`, exports `site/index.html`, runs `verify_editor_deployment.py --share-only`, and uploads the `site/` artifact.

## Local Live App

```bash
make run
```

Open `http://localhost:2718`. By default this keeps Marimo token/skew protections enabled. For trusted local-only development, you can intentionally pass Marimo flags yourself or use `run.py --no-token` with a localhost bind.

## Local Editor

```bash
make edit
```

For VS Code/Cursor, install the official `marimo-team.vscode-marimo` extension and select the project interpreter at `.venv/bin/python`.

## Full Verification

```bash
make verify
```

This checks:

- Python syntax and `marimo check app.py`
- App structure and `ipk_head.html` runtime markers
- README, Makefile, Dockerfile, GitHub Pages workflow, and static site markers
- Static HTML export to `/tmp/ipk_editor_deployment_verify.html`
- Jupyter `.ipynb` export to `/tmp/ipk_editor_deployment_verify.ipynb`
- Headless `marimo edit` health
- Local app health at `http://localhost:2718/health` when available
- VS Code / JupyterLab host-tool readiness as warnings unless `--strict-host-tools` is passed

Fast share-only verification:

```bash
./.venv/bin/python verify_editor_deployment.py --share-only
```

## Docker / Live Hosting

Build and run locally behind trusted ingress:

```bash
docker build -t intelligent-physics-kernel:latest .
docker run --rm -p 127.0.0.1:2718:2718 intelligent-physics-kernel:latest
```

Or with Compose:

```bash
docker compose up --build
```

The Compose file binds to `127.0.0.1`, drops Linux capabilities, uses `no-new-privileges`, runs read-only with `/tmp` as tmpfs, and restarts unless stopped.

For public live hosting:

- Put the app behind HTTPS and authentication.
- Keep direct container binding private, or expose only through a reverse proxy/load balancer.
- Configure Marimo auth/token-password support or platform auth.
- Do not publish a no-token public Python kernel.

## Jupyter / JupyterHub

Install the Jupyter bridge dependencies from `requirements-jupyterhub.txt` in the relevant host environment. For multi-environment JupyterHub, install `marimo` in the user's environment and `marimo-jupyter-extension` in the Jupyter environment. If Marimo is not on `PATH`, adapt `jupyterhub_config.py.sample` and set `MarimoProxyConfig.marimo_path` to the deployed environment's `marimo` executable.

## References

- Marimo static HTML: https://docs.marimo.io/guides/exporting/static_html/
- Marimo WebAssembly HTML export: https://docs.marimo.io/guides/exporting/webassembly_html/
- Marimo Docker deployment: https://docs.marimo.io/guides/deploying/deploying_docker/
- Marimo GitHub Pages publishing: https://docs.marimo.io/guides/publishing/github/
- GitHub Pages publishing sources: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
