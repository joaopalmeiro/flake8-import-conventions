import ast
from typing import List, Tuple

import attr

from .errors import name2asname, name2message


# Based on:
# - https://github.com/deppen8/pandas-vet/blob/master/pandas_vet/__init__.py#L132
def check_import_name(node: ast.Import) -> List[Tuple[int, int, str]]:
    errors = []

    for n in node.names:
        if n.name in name2asname and n.asname != name2asname[n.name]:
            errors.append((node.lineno, node.col_offset, name2message[n.name]))

    return errors


@attr.s
class Visitor(ast.NodeVisitor):
    errors: List[Tuple[int, int, str]] = attr.ib(factory=list)

    # More info: https://docs.python.org/3/library/ast.html#ast.Import
    def visit_Import(self, node: ast.Import) -> None:
        # Called for `import ..` and `import .. as ..` nodes
        self.generic_visit(node)  # Continue checking children
        self.errors.extend(check_import_name(node))
