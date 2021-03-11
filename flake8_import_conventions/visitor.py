import ast
from typing import List, Tuple

import attr


# Based on: https://github.com/deppen8/pandas-vet/blob/master/pandas_vet/__init__.py#L132
def check_import_name(node: ast.Import) -> List[Tuple[int, int, str]]:
    pass


@attr.s
class Visitor(ast.NodeVisitor):
    errors: List[Tuple[int, int, str]] = attr.ib(factory=list)

    # More info: https://docs.python.org/3/library/ast.html#ast.Import
    def visit_Import(self, node: ast.Import) -> None:
        # Called for `import ..` and `import .. as ..` nodes
        pass
