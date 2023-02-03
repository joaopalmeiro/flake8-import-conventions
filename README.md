# flake8-import-conventions

[![PyPI](https://img.shields.io/pypi/v/flake8-import-conventions.svg)](https://pypi.org/project/flake8-import-conventions/)

An opinionated plugin for Flake8 on how certain packages should be imported or aliased.

It is based on the [`pandas-vet`](https://github.com/deppen8/pandas-vet) and [`flake8-2020`](https://github.com/asottile/flake8-2020) plugins.

## Installation

Via [Pipenv](https://pipenv.pypa.io/):

```bash
pipenv install --dev flake8 flake8-import-conventions
```

## Development

```bash
poetry install --with dev
```

```bash
poetry shell
```

Open the `manual_test.py` file in VS Code to see the error messages.

```bash
pytest tests/ -v
```

or (to see `print()`s)

```bash
pytest tests/ -v -s
```

## Deployment

```bash
poetry check
```

```bash
poetry version minor
```

or

```bash
poetry version patch
```

```bash
git tag
```

```bash
git tag "v$(poetry version --short)"
```

```bash
git push origin "v$(poetry version --short)"
```

## References

- Anthony Sottile's "[a flake8 plugin from scratch (intermediate) anthony explains #025](https://youtu.be/ot5Z4KQPBL8)" tutorial.
- [flake8-pie](https://github.com/sbdchd/flake8-pie).
- [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide).
