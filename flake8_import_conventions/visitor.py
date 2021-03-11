import ast
from typing import List

import attr


def check_import_name(node: ast.Import) -> List:
    pass


@attr.s
class Visitor(ast.NodeVisitor):
    errors = attr.ib(factory=list)

    # More info: https://docs.python.org/3/library/ast.html#ast.Import
    def visit_Import(self, node: ast.Import) -> None:
        """
        Called for `import ..` and `import .. as ..` nodes.
        """
        pass
