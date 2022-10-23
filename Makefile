.PHONY: black-check
black-check:
	poetry run black --check src/stacks src/sample_minimal_lambda tests app.py

.PHONY: black
black:
	poetry run black src/stacks src/sample_minimal_lambda tests app.py

.PHONY: flake8
flake8:
	poetry run flake8 src/stacks src/sample_minimal_lambda tests app.py

.PHONY: isort-check
isort-check:
	poetry run isort --check-only src/stacks src/sample_minimal_lambda tests app.py

.PHONY: isort
isort:
	poetry run isort src/stacks src/sample_minimal_lambda tests app.py

.PHONY: mypy
mypy:
	poetry run mypy src/stacks src/sample_minimal_lambda app.py

.PHONY: test
test:
	poetry run pytest tests --cov=src --cov-report term-missing --durations 5

.PHONY: format
format:
	$(MAKE) black
	$(MAKE) isort

.PHONY: lint
lint:
	$(MAKE) black-check
	$(MAKE) isort-check
	$(MAKE) flake8
	$(MAKE) mypy

.PHONY: test-all
test-all:
	$(MAKE) lint
	$(MAKE) test