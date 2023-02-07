# Notes

- [flake8-class-attributes-order](https://github.com/best-doctor/flake8-class-attributes-order).
- [astpretty](https://github.com/asottile/astpretty).
- [babi](https://github.com/asottile/babi) (text editor).
- `self.generic_visit(node)`: call it at the end of each `visit_*` method for the recursion to continue.
- [attrs](https://www.attrs.org/):
  - "Classes without boilerplate".
  - No need to implement object protocols (dunder methods).
  - "It does _nothing_ dynamic at runtime, hence zero runtime overhead."
  - `__attrs_post_init__` method.
- [Dict vs. slotted classes](https://www.attrs.org/en/stable/glossary.html).
- `poetry add flake8@^3.0.0 attrs`.
- `flake8 formatter.py flake8_import_conventions --jobs 1`.
- `poetry install --no-root` (don't install _this_ package).
- `import typing as t` ([flake8-annotations](https://github.com/sco1/flake8-annotations)).
- `import geopandas` ([source](https://github.com/geopandas/geopandas/issues/716)).
- https://github.com/asottile/flake8-2020/commit/10ba36520cca00ecbc812b2b96fcaaf9f8999c06
- Poetry:
  - https://python-poetry.org/docs/#installing-with-the-official-installer
  - `poetry --version` (1.3.2)
  - `poetry init` (https://python-poetry.org/docs/basic-usage/#initialising-a-pre-existing-project)
  - https://python-poetry.org/docs/dependency-specification/#exact-requirements
  - `poetry add attrs`
  - `poetry add mypy black bandit pytest --group dev`
  - `poetry add isort@^5.11.5 --group dev` or `poetry add isort --group dev --allow-prereleases` (https://github.com/PyCQA/isort/issues/2084 + https://pypi.org/project/isort/6.0.0b2/#history + https://github.com/PyCQA/isort/issues/2083)
  - `flake8 = ">=5"` (https://github.com/asottile/flake8-2020/blob/v1.7.0/setup.cfg#L25)
  - https://python-poetry.org/docs/cli/#add (_Allow >=2.0.5 versions, without upper bound_)
  - `poetry config virtualenvs.in-project true --local`
  - `poetry env remove --all`
  - `poetry config --list`
  - https://python-poetry.org/docs/pyproject/#classifiers
  - `poetry add tomark --group dev`
- https://www.attrs.org/en/latest/index.html#getting-started
- Delete local tag: `git tag -d v0.0.1`
- `import seaborn as sns`: https://seaborn.pydata.org/installing.html
- Path: `/mnt/c/Users/johnn/Documents/GitHub/flake8-import-conventions`
- https://import-as.github.io/
- https://github.com/marcgibbons/flake8-datetime-import

## Snippets

**Minimal boilerplate for the `Plugin` class**:

```python
import ast
import importlib.metadata
from typing import Any, Generator, Tuple, Type


class Plugin:
    name = __name__
    version = importlib.metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        # The AST that represents a single file
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        # Tuple[line number, character offset, message]
        # Type[Any] is not being used (use `type(self)`)
        pass
```

**Syntactic sugar for `attr.ib(default=attr.Factory(f))`**:

```python
@attr.s
class C(object):
    x = attr.ib(factory=list)
    # instead of
    # x = attr.ib(default=attr.Factory(list))
```

**`from X import ...` is not allowed. `X` must be imported as a module.** (from Marc Gibbons' [flake8-datetime-import](https://github.com/marcgibbons/flake8-datetime-import) plugin):

```python
ERRORS = {
    "DTI100": (
        "`from datetime import ...` is not allowed. `datetime` must be "
        "imported as a module."
    ),
}


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.problems = []

    def visit_ImportFrom(self, node):
        if node.module == "datetime":
            self.problems.append((node.lineno, node.col_offset, "DTI100"))
        if node.module == "time":
            self.problems.append((node.lineno, node.col_offset, "DTI200"))

        self.generic_visit(node)
```
