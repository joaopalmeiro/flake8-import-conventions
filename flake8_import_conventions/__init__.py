import ast
import sys
from typing import Any, Generator, Tuple, Type

from .visitor import Visitor

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata

__version__ = importlib_metadata.version(__name__)


# Based on: https://github.com/asottile/flake8-2020/blob/master/flake8_2020.py#L160
# The plugin class must be in the `__init__` file
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
