# flake8-import-conventions

An opinionated plugin for Flake8 on how certain packages should be imported or aliased.

It is based on the [`pandas-vet`](https://github.com/deppen8/pandas-vet) plugin.

## References

- Anthony Sottile's "[a flake8 plugin from scratch (intermediate) anthony explains #025](https://youtu.be/ot5Z4KQPBL8)" tutorial.

## Notes

- [flake8-class-attributes-order](https://github.com/best-doctor/flake8-class-attributes-order).
- [astpretty](https://github.com/asottile/astpretty).
- [babi](https://github.com/asottile/babi) (text editor).
- `self.generic_visit(node)`: call it at the end of each `visit_*` method for the recursion to continue.

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
