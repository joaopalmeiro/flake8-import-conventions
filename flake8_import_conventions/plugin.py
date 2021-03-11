import ast
from typing import Any, Generator, Tuple, Type

from . import __name__, __version__
from .visitor import Visitor


# Based on: https://github.com/asottile/flake8-2020/blob/master/flake8_2020.py#L160
class Plugin:
    # name = __name__
    name = __name__.replace("_", "-")
    version = __version__

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)
