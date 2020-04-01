VERSION=$(shell python -c 'import toml; print(toml.load("pyproject.toml")["tool"]["poetry"]["version"])')
SRCDIRS=specs src tests

test:
	pytest --exitfirst --forked --capture=no \
		--cov --cov-branch --cov-report=term --cov-report=xml

type:
	MYPYPATH=./src mypy -p ingraph

format:
	black --include '\.pyi?$$' $(SRCDIRS)
	autoflake -ri $(SRCDIRS)
	isort -rc $(SRCDIRS)
	npx prettier --end-of-line lf --write '**/*.{css,html,js,json,md,yaml,yml}'
	sed -i "s/version-[0-9]\+.[0-9]\+.[0-9]\+/version-$(VERSION)/g" README.md
	sed -i "s/ingraph\/[0-9]\+.[0-9]\+.[0-9]\+/ingraph\/$(VERSION)/g" README.md

spec:
	python -m specs.aws

clean:
	rm -rf .coverage* .mypy_cache .pytest_cache coverage.xml dist
	find . -name __pycache__ -o -name *.egg-info | xargs rm -rf

install:
	poetry install

dist: clean install format type test
	poetry build
	cd scaffold; make clean
	cp -r scaffold dist/helloworld
	cd dist; zip -r ingraph-helloworld.zip helloworld
	rm -rf dist/helloworld

.PHONY: dist
