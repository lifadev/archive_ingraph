build:
	ig cfn -i helloworld.example -r Example -o build/example.yaml

.PHONY: build

type:
	MYPYPATH=./src mypy -p helloworld

format:
	black --include '\.pyi?$$' src
	autoflake -ri src
	isort -rc src
	npx prettier --end-of-line lf --write '**/*.{css,html,js,json,md,yaml,yml}'

install:
	poetry install

clean:
	rm -rf .mypy_cache build dist
	find . -name __pycache__ -o -name *.egg-info | xargs rm -rf

dist: clean install format type
	poetry build

.PHONY: dist
