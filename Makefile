PYTHON ?= ./.venv/bin/python
PORT ?= 2718
STATIC_PORT ?= 8000

.PHONY: install run edit verify site serve-site docker-build docker-run clean-site

install:
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) -m marimo run app.py --port $(PORT)

edit:
	$(PYTHON) -m marimo edit app.py --port $(PORT)

verify:
	$(PYTHON) -m py_compile app.py verify_editor_deployment.py
	$(PYTHON) -m marimo check app.py
	$(PYTHON) verify_editor_deployment.py

verify-share:
	$(PYTHON) verify_editor_deployment.py --share-only

site:
	mkdir -p site
	$(PYTHON) -m marimo export html app.py -o site/index.html --no-include-code -f
	$(PYTHON) -c 'from pathlib import Path; p=Path("site/index.html"); s=p.read_text(); s=s.replace("<meta name=\"description\" content=\"a marimo app\" />", "<meta name=\"description\" content=\"Interactive Intelligent Physics Kernel notebook: MU, E8, Spin(10), Standard Model, derivation forest, and falsification dashboard.\" />"); p.write_text(s)'
	touch site/.nojekyll

serve-site: site
	$(PYTHON) -m http.server $(STATIC_PORT) --directory site

docker-build:
	docker build -t intelligent-physics-kernel:latest .

docker-run:
	docker run --rm -p 127.0.0.1:$(PORT):2718 intelligent-physics-kernel:latest

clean-site:
	rm -rf site
