.PHONY: clean
clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .mypy_cache

.PHONY: venv
venv:
	python3 -m venv .venv

.PHONY: venv-activate
venv-activate:
	. .venv/bin/activate

.PHONY: install
install:
	python3 -m pip install .

.PHONY: install-editable
install-editable:
	python3 -m pip install -e .

.PHONY: install-test
install-test:
	python3 -m pip install -e .[test]

.PHONY: test
test:
	python -m pytest tests

.PHONY: build
build:
	docker build -f ./db/Dockerfile -t pg-db .

.PHONY: run-db
run-db:
	docker run --rm --name postgres_db -p 5000:5432 -d pg-db

.PHONY: etl
etl:
	. ./run.sh
