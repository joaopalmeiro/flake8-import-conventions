import ast
from typing import Any, Generator, Tuple, Type

from .visitor import Visitor

# https://github.com/asottile/flake8-2020/commit/10ba36520cca00ecbc812b2b96fcaaf9f8999c06
# https://flake8.pycqa.org/en/latest/plugin-development/registering-plugins.html
# https://github.com/asottile/flake8-2020/blob/v1.7.0/setup.cfg


# Based on:
# - https://github.com/asottile/flake8-2020/blob/v1.6.0/flake8_2020.py#L160
# - https://github.com/asottile/flake8-2020/blob/v1.7.0/flake8_2020.py#L150
# The plugin class must be in the `__init__` file
class Plugin:
    # name = __name__
    # name = __name__.replace("_", "-")
    # version = __version__

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)
