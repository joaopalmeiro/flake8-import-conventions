# flake8-import-conventions

An opinionated plugin for Flake8 on how certain packages should be imported or aliased.

It is based on the [`pandas-vet`](https://github.com/deppen8/pandas-vet) and [`flake8-2020`](https://github.com/asottile/flake8-2020) plugins.

## References

- Anthony Sottile's "[a flake8 plugin from scratch (intermediate) anthony explains #025](https://youtu.be/ot5Z4KQPBL8)" tutorial.
- [flake8-pie](https://github.com/sbdchd/flake8-pie).
- [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide).

## Notes

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
