# flake8-import-conventions

[![PyPI](https://img.shields.io/pypi/v/flake8-import-conventions.svg)](https://pypi.org/project/flake8-import-conventions/)

<p align="center">
  <img alt="" src="https://raw.githubusercontent.com/joaopalmeiro/flake8-import-conventions/main/assets/logo_round.png" width="100" height="100" />
</p>

An opinionated plugin for Flake8 on how certain packages should be imported or aliased.

It is based on the [`pandas-vet`](https://github.com/deppen8/pandas-vet) and [`flake8-2020`](https://github.com/asottile/flake8-2020) plugins.

## Installation

Via [Pipenv](https://pipenv.pypa.io/):

```bash
pipenv install --dev flake8 flake8-import-conventions
```

## Flake8 codes

| Package                                 | Code  | Description                                           |
| --------------------------------------- | ----- | ----------------------------------------------------- |
| [Altair](https://altair-viz.github.io/) | IC001 | altair should be imported as `import altair as alt`   |
| [GeoPandas](https://geopandas.org/)     | IC002 | geopandas should be imported as `import geopandas`    |
| [NumPy](https://numpy.org/)             | IC003 | numpy should be imported as `import numpy as np`      |
| [pandas](https://pandas.pydata.org/)    | IC004 | pandas should be imported as `import pandas as pd`    |
| [seaborn](https://seaborn.pydata.org/)  | IC005 | seaborn should be imported as `import seaborn as sns` |

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

Copy the output of the following script and paste it in the [Flake8 codes](#flake8-codes) section:

```bash
python gen_table.py
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
