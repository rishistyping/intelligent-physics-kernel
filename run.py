#!/usr/bin/env python3
"""
Convenience launcher for the Intelligent Physics Kernel notebook.

Usage:
    python run.py          # Run as read-only app (recommended)
    python run.py --edit   # Open in Marimo editor
"""

import argparse
import sys
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Launch the Intelligent Physics Kernel Marimo notebook.")
    parser.add_argument("--edit", action="store_true", help="Open the notebook in Marimo edit mode.")
    parser.add_argument("--host", default=None, help="Host interface to bind, e.g. 0.0.0.0 for deployment.")
    parser.add_argument("--port", default="2718", help="Port to bind. Defaults to 2718.")
    parser.add_argument("--token", action="store_true", help="Require Marimo's access token.")
    parser.add_argument("--no-token", action="store_true", help="Disable Marimo's access token for trusted local-only use.")
    parser.add_argument("--skew-protection", action="store_true", help="Enable Marimo's stale-client skew protection.")
    parser.add_argument("--no-skew-protection", action="store_true", help="Disable stale-client skew protection for trusted local-only use.")
    args = parser.parse_args()

    python = sys.executable
    if args.edit:
        cmd = [python, "-m", "marimo", "edit", "app.py", "--port", args.port]
    else:
        cmd = [python, "-m", "marimo", "run", "app.py", "--port", args.port]

    if args.host:
        cmd.extend(["--host", args.host])
    public_bind = args.host in {"0.0.0.0", "::"}
    if args.no_token and not public_bind:
        cmd.append("--no-token")
    elif args.no_token and public_bind:
        print("Refusing --no-token with a public host bind. Use 127.0.0.1 or keep token protection.", file=sys.stderr)
        return 2

    if args.skew_protection:
        pass
    elif args.no_skew_protection and not public_bind:
        cmd.append("--no-skew-protection")
    elif args.no_skew_protection and public_bind:
        print("Refusing --no-skew-protection with a public host bind. Use 127.0.0.1 or keep skew protection.", file=sys.stderr)
        return 2

    print("Launching:", " ".join(cmd))
    raise SystemExit(subprocess.run(cmd).returncode)

if __name__ == "__main__":
    raise SystemExit(main())
