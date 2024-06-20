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

.PHONY: install
install:
	. .venv/bin/activate
	python3 -m pip install .

.PHONY: install-editable
install-editable:
	. .venv/bin/activate
	python3 -m pip install -e .

.PHONY: install-test
install-test:
	. .venv/bin/activate
	python3 -m pip install -e .[test]

.PHONY: test
test:
	python -m pytest tests