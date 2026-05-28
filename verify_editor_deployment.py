#!/usr/bin/env python3
"""
Repeatable local verification for the Intelligent Physics Kernel marimo app.

This script checks the parts of the VS Code / JupyterHub story that can be
proven locally without opening those host UIs:

- Python syntax and marimo static analysis
- app structure and custom head runtime markers
- VS Code / JupyterHub support files
- HTML export
- Jupyter .ipynb export
- headless marimo edit server health
- optional LaunchAgent health
- local availability of VS Code / Jupyter command-line tools
"""

from __future__ import annotations

import argparse
import ast
import json
import shutil
import socket
import subprocess
import sys
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parent
APP = ROOT / "app.py"
HTML_HEAD = ROOT / "ipk_head.html"
JUPYTERHUB_REQUIREMENTS = ROOT / "requirements-jupyterhub.txt"
JUPYTERHUB_CONFIG_SAMPLE = ROOT / "jupyterhub_config.py.sample"
VSCODE_SETTINGS = ROOT / ".vscode" / "settings.json"
VSCODE_EXTENSIONS = ROOT / ".vscode" / "extensions.json"
README = ROOT / "README.md"
MAKEFILE = ROOT / "Makefile"
PAGES_WORKFLOW = ROOT / ".github" / "workflows" / "pages-static.yml"
DOCKERFILE = ROOT / "Dockerfile"
SITE_INDEX = ROOT / "site" / "index.html"
TMP_HTML = Path("/tmp/ipk_editor_deployment_verify.html")
TMP_IPYNB = Path("/tmp/ipk_editor_deployment_verify.ipynb")
LAUNCH_AGENT_URL = "http://localhost:2718/health"
MIN_APP_CELLS = 5
PUBLIC_DESCRIPTION = (
    "Interactive Intelligent Physics Kernel notebook: MU, E8, Spin(10), "
    "Standard Model, derivation forest, and falsification dashboard."
)


@dataclass
class CheckResult:
    name: str
    status: str
    detail: str


def _read_text(path: Path, name: str) -> tuple[str | None, CheckResult | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except FileNotFoundError:
        return None, CheckResult(name, "FAIL", f"{path} missing")
    except OSError as exc:
        return None, CheckResult(name, "FAIL", f"could not read {path.name}: {exc}")


def _run(cmd: Sequence[str], timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(cmd),
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )


def _polish_static_html(path: Path) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        '<meta name="description" content="a marimo app" />',
        f'<meta name="description" content="{PUBLIC_DESCRIPTION}" />',
    )
    path.write_text(text, encoding="utf-8")


def _health(url: str, timeout: float = 3.0) -> tuple[bool, str]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.status == 200, body.strip()
    except Exception as exc:  # pragma: no cover - diagnostic path
        return False, f"{type(exc).__name__}: {exc}"


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _append_process_result(results: list[CheckResult], name: str, proc: subprocess.CompletedProcess[str]) -> None:
    detail = (proc.stdout or proc.stderr or "").strip()
    if len(detail) > 500:
        detail = detail[:500] + "..."
    results.append(CheckResult(name, "PASS" if proc.returncode == 0 else "FAIL", detail or "ok"))


def _keyword_string(call: ast.Call, name: str) -> str | None:
    for keyword in call.keywords:
        if (
            keyword.arg == name
            and isinstance(keyword.value, ast.Constant)
            and isinstance(keyword.value.value, str)
        ):
            return keyword.value.value
    return None


def _is_marimo_app_call(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "App"
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "marimo"
    )


def _is_app_cell_decorator(node: ast.AST) -> bool:
    decorator = node.func if isinstance(node, ast.Call) else node
    return (
        isinstance(decorator, ast.Attribute)
        and decorator.attr == "cell"
        and isinstance(decorator.value, ast.Name)
        and decorator.value.id == "app"
    )


def _check_app_artifacts() -> list[CheckResult]:
    source, failure = _read_text(APP, "marimo app artifact")
    if failure:
        return [failure]
    assert source is not None

    try:
        tree = ast.parse(source, filename=str(APP))
    except SyntaxError as exc:
        return [CheckResult("marimo app artifact", "FAIL", f"could not parse app.py: {exc}")]

    app_calls = [node for node in ast.walk(tree) if _is_marimo_app_call(node)]
    configured_call = next(
        (
            call
            for call in app_calls
            if _keyword_string(call, "width") == "full"
            and _keyword_string(call, "html_head_file") == HTML_HEAD.name
        ),
        None,
    )
    if configured_call:
        config_result = CheckResult(
            "marimo App configuration",
            "PASS",
            f'width="full"; html_head_file="{HTML_HEAD.name}"',
        )
    elif app_calls:
        details = [
            (
                f"width={_keyword_string(call, 'width')!r}, "
                f"html_head_file={_keyword_string(call, 'html_head_file')!r}"
            )
            for call in app_calls
        ]
        config_result = CheckResult("marimo App configuration", "FAIL", "; ".join(details))
    else:
        config_result = CheckResult("marimo App configuration", "FAIL", "no marimo.App(...) call found")

    cell_count = sum(
        1
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and any(_is_app_cell_decorator(decorator) for decorator in node.decorator_list)
    )
    cell_result = CheckResult(
        "marimo cell app structure",
        "PASS" if cell_count > MIN_APP_CELLS else "FAIL",
        f"@app.cell decorators={cell_count}; expected>{MIN_APP_CELLS}",
    )
    return [config_result, cell_result]


def _check_html_head_artifact() -> list[CheckResult]:
    text, failure = _read_text(HTML_HEAD, "ipk_head.html artifact")
    if failure:
        return [failure]
    assert text is not None

    results = [
        CheckResult(
            "ipk_head.html artifact",
            "PASS" if text.strip() else "FAIL",
            f"{HTML_HEAD}; bytes={len(text.encode('utf-8'))}",
        )
    ]
    marker_groups = {
        "II motion/runtime": ("__ipkIIMotionBootstrap", "__ipkIIMotionInstalled"),
        "cursor": ("#cursor-dot", "cursorDot", "cursor-ripple"),
        "progress": ("#read-progress", "read-progress"),
        "ripple": ("ipk-ripple-wave", "cursor-ripple"),
        "spotlight": ("--spot-x", "--spot-y"),
    }
    missing = [
        name
        for name, markers in marker_groups.items()
        if not any(marker in text for marker in markers)
    ]
    results.append(
        CheckResult(
            "ipk_head.html runtime markers",
            "PASS" if not missing else "FAIL",
            (
                "found II/cursor/progress/ripple/spotlight markers"
                if not missing
                else f"missing: {', '.join(missing)}"
            ),
        )
    )
    return results


def _check_support_files() -> list[CheckResult]:
    results: list[CheckResult] = []

    text, failure = _read_text(JUPYTERHUB_REQUIREMENTS, "JupyterHub requirements")
    if failure:
        results.append(failure)
    else:
        assert text is not None
        text = text.lower()
        missing = [
            requirement
            for requirement in ("jupyterhub", "jupyterlab", "marimo", "marimo-jupyter-extension")
            if requirement not in text
        ]
        results.append(
            CheckResult(
                "JupyterHub requirements",
                "PASS" if not missing else "FAIL",
                (
                    "contains marimo/JupyterHub editor dependencies"
                    if not missing
                    else f"missing: {', '.join(missing)}"
                ),
            )
        )

    text, failure = _read_text(JUPYTERHUB_CONFIG_SAMPLE, "JupyterHub config sample")
    if failure:
        results.append(failure)
    else:
        assert text is not None
        missing = [
            marker
            for marker in ("MarimoProxyConfig.marimo_path", "MarimoProxyConfig.timeout")
            if marker not in text
        ]
        results.append(
            CheckResult(
                "JupyterHub config sample",
                "PASS" if not missing else "FAIL",
                (
                    "contains marimo proxy path and timeout"
                    if not missing
                    else f"missing: {', '.join(missing)}"
                ),
            )
        )

    text, failure = _read_text(VSCODE_SETTINGS, "VS Code workspace settings")
    if failure:
        results.append(failure)
    else:
        assert text is not None
        try:
            settings = json.loads(text)
            missing = [
                key
                for key in ("python.defaultInterpreterPath", "marimo.pythonPath")
                if key not in settings
            ]
            results.append(
                CheckResult(
                    "VS Code workspace settings",
                    "PASS" if not missing else "FAIL",
                    (
                        "contains Python and marimo interpreter paths"
                        if not missing
                        else f"missing: {', '.join(missing)}"
                    ),
                )
            )
        except json.JSONDecodeError as exc:
            results.append(CheckResult("VS Code workspace settings", "FAIL", f"invalid JSON: {exc}"))

    text, failure = _read_text(VSCODE_EXTENSIONS, "VS Code extension recommendations")
    if failure:
        results.append(failure)
    else:
        assert text is not None
        try:
            extensions = json.loads(text)
            recommendations = extensions.get("recommendations", [])
            installed = (
                isinstance(recommendations, list)
                and "marimo-team.vscode-marimo" in recommendations
            )
            results.append(
                CheckResult(
                    "VS Code extension recommendations",
                    "PASS" if installed else "FAIL",
                    (
                        "recommends marimo-team.vscode-marimo"
                        if installed
                        else "marimo-team.vscode-marimo not recommended"
                    ),
                )
            )
        except json.JSONDecodeError as exc:
            results.append(CheckResult("VS Code extension recommendations", "FAIL", f"invalid JSON: {exc}"))

    return results


def _check_static_html(path: Path, name: str, require_nojekyll: bool = False) -> list[CheckResult]:
    results: list[CheckResult] = []
    text, failure = _read_text(path, name)
    if failure:
        return [failure]
    assert text is not None
    markers = (
        "Intelligent Physics Kernel",
        "Derivation Trees Explorer",
        "ipk-forest-panel",
        "__ipkIIMotionBootstrap",
        "Vocabulary lawful",
        "Falsification Kill List",
    )
    missing = [marker for marker in markers if marker not in text]
    forbidden = [
        marker
        for marker in (
            "Traceback (most recent call last)",
            "Minified React error",
            "An internal error occurred",
            'content="a marimo app"',
            "/Users/",
        )
        if marker in text
    ]
    size_ok = path.exists() and path.stat().st_size > 100_000
    status = "PASS" if not missing and not forbidden and size_ok else "FAIL"
    detail = (
        f"{path}; bytes={path.stat().st_size}"
        if status == "PASS"
        else f"missing={missing}; forbidden={forbidden}; bytes={path.stat().st_size if path.exists() else 0}"
    )
    results.append(CheckResult(name, status, detail))
    if require_nojekyll:
        nojekyll = path.parent / ".nojekyll"
        results.append(
            CheckResult(
                "static site .nojekyll",
                "PASS" if nojekyll.exists() else "FAIL",
                str(nojekyll),
            )
        )
    return results


def _check_public_share_files() -> list[CheckResult]:
    results: list[CheckResult] = []

    checks = [
        (
            README,
            "public README",
            (
                "Quick Start",
                "Publish A Static Site",
                "Full Live Deployment",
                "make site",
                "make verify-share",
                ".github/workflows/pages-static.yml",
                "auth/TLS",
            ),
            "documents run, static publish, and live deployment paths",
        ),
        (
            MAKEFILE,
            "Makefile share helpers",
            (
                "verify:",
                "verify_editor_deployment.py",
                "marimo check",
                "site:",
                "--no-include-code",
                "touch site/.nojekyll",
                "serve-site:",
                "docker-build:",
                "127.0.0.1:$(PORT):2718",
            ),
            "contains verify/site/serve/docker helpers",
        ),
        (
            PAGES_WORKFLOW,
            "GitHub Pages workflow",
            (
                "actions/deploy-pages",
                "actions/upload-pages-artifact",
                "python -m py_compile app.py verify_editor_deployment.py",
                "python -m marimo export html app.py",
                "python verify_editor_deployment.py --share-only",
                "touch site/.nojekyll",
                "path: site",
                "permissions:",
                "verify_editor_deployment.py",
            ),
            "checks and deploys static Marimo export",
        ),
        (
            DOCKERFILE,
            "Docker production baseline",
            (
                "USER marimo",
                "HEALTHCHECK",
                "marimo",
                "--host",
                "0.0.0.0",
            ),
            "runs as non-root with Marimo healthcheck",
        ),
    ]
    for path, name, markers, pass_detail in checks:
        text, failure = _read_text(path, name)
        if failure:
            results.append(failure)
            continue
        assert text is not None
        missing = [marker for marker in markers if marker not in text]
        results.append(
            CheckResult(
                name,
                "PASS" if not missing else "FAIL",
                pass_detail if not missing else f"missing: {', '.join(missing)}",
            )
        )

    if SITE_INDEX.exists():
        results.extend(_check_static_html(SITE_INDEX, "generated static site", require_nojekyll=True))
    else:
        results.append(CheckResult("generated static site", "WARN", "site/index.html not built; run `make site`"))

    return results


def _check_edit_server(python: str, timeout: int = 45) -> CheckResult:
    port = _free_port()
    proc = subprocess.Popen(
        [
            python,
            "-m",
            "marimo",
            "edit",
            str(APP),
            "--headless",
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
            "--no-token",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    try:
        deadline = time.time() + timeout
        last_body = "no response yet"
        while time.time() < deadline:
            ok, body = _health(f"http://localhost:{port}/health")
            last_body = body
            if ok:
                return CheckResult("headless marimo edit health", "PASS", f"port {port}: {body}")
            if proc.poll() is not None:
                stdout, stderr = proc.communicate(timeout=2)
                detail = (stderr or stdout or last_body).strip()
                return CheckResult("headless marimo edit health", "FAIL", detail or "server exited")
            time.sleep(0.5)
        return CheckResult("headless marimo edit health", "FAIL", f"timed out waiting for port {port}: {last_body}")
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=5)


def run_checks(strict_host_tools: bool, share_only: bool = False) -> tuple[int, list[CheckResult]]:
    python = sys.executable
    results: list[CheckResult] = []

    for path in (TMP_HTML, TMP_IPYNB):
        if path.exists():
            path.unlink()

    results.extend(_check_app_artifacts())
    results.extend(_check_html_head_artifact())
    results.extend(_check_support_files())
    results.extend(_check_public_share_files())

    if share_only:
        failures = [result for result in results if result.status == "FAIL"]
        return (1 if failures else 0), results

    _append_process_result(results, "python syntax", _run([python, "-m", "py_compile", str(APP)], timeout=60))
    _append_process_result(results, "marimo check", _run([python, "-m", "marimo", "check", str(APP)], timeout=120))
    _append_process_result(
        results,
        "static HTML export",
        _run(
            [
                python,
                "-m",
                "marimo",
                "export",
                "html",
                str(APP),
                "-o",
                str(TMP_HTML),
                "--no-include-code",
            ],
            timeout=180,
        ),
    )
    _polish_static_html(TMP_HTML)
    results.append(CheckResult("static HTML artifact", "PASS" if TMP_HTML.exists() and TMP_HTML.stat().st_size > 100_000 else "FAIL", str(TMP_HTML)))
    if TMP_HTML.exists():
        results.extend(_check_static_html(TMP_HTML, "temporary static HTML content"))

    _append_process_result(
        results,
        "Jupyter ipynb export",
        _run([python, "-m", "marimo", "export", "ipynb", str(APP), "-o", str(TMP_IPYNB)], timeout=180),
    )
    ipynb_ok = False
    if TMP_IPYNB.exists():
        try:
            data = json.loads(TMP_IPYNB.read_text())
            ipynb_ok = data.get("nbformat") == 4 and len(data.get("cells", [])) > 5
            detail = f"{TMP_IPYNB}; cells={len(data.get('cells', []))}"
        except Exception as exc:
            detail = f"{TMP_IPYNB}; parse failed: {exc}"
    else:
        detail = f"{TMP_IPYNB} missing"
    results.append(CheckResult("Jupyter ipynb artifact", "PASS" if ipynb_ok else "FAIL", detail))

    results.append(_check_edit_server(python))

    ok, body = _health(LAUNCH_AGENT_URL)
    results.append(CheckResult("LaunchAgent app health", "PASS" if ok else "WARN", body))

    code = shutil.which("code")
    if code:
        proc = _run([code, "--list-extensions"], timeout=30)
        installed = "marimo-team.vscode-marimo" in proc.stdout
        status = "PASS" if installed else ("FAIL" if strict_host_tools else "WARN")
        results.append(CheckResult("VS Code marimo extension", status, "installed" if installed else "code CLI present; marimo extension not listed"))
    else:
        results.append(CheckResult("VS Code CLI", "FAIL" if strict_host_tools else "WARN", "code command not found; manual VS Code UI check still required"))

    jupyter = shutil.which("jupyter")
    if jupyter:
        proc = _run([jupyter, "labextension", "list"], timeout=45)
        output = proc.stdout + proc.stderr
        installed = "marimo" in output.lower()
        status = "PASS" if installed else ("FAIL" if strict_host_tools else "WARN")
        results.append(CheckResult("JupyterLab marimo extension", status, "listed" if installed else "jupyter CLI present; marimo extension not listed"))
    else:
        results.append(CheckResult("Jupyter CLI", "FAIL" if strict_host_tools else "WARN", "jupyter command not found; JupyterHub host check still required"))

    failures = [result for result in results if result.status == "FAIL"]
    return (1 if failures else 0), results


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify local marimo editor/deployment readiness.")
    parser.add_argument(
        "--strict-host-tools",
        action="store_true",
        help="Fail if VS Code or JupyterLab host integrations are not installed locally.",
    )
    parser.add_argument(
        "--share-only",
        action="store_true",
        help="Run only artifact/docs/static-site checks suitable for CI public-share gating.",
    )
    args = parser.parse_args()

    code, results = run_checks(strict_host_tools=args.strict_host_tools, share_only=args.share_only)
    width = max(len(result.name) for result in results)
    for result in results:
        print(f"{result.status:<4} {result.name:<{width}}  {result.detail}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
