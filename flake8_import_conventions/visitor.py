import ast
from typing import List, Tuple

# import attr
from attrs import Factory, define

from .errors import name2asname, name2message


# Based on:
# - https://github.com/deppen8/pandas-vet/blob/v0.2.3/pandas_vet/__init__.py#L139
# - https://github.com/deppen8/pandas-vet/blob/v0.2.3/pandas_vet/__init__.py#L12
def check_import_name(node: ast.Import) -> List[Tuple[int, int, str]]:
    errors = []
    # https://docs.python.org/3.7/library/ast.html#ast.dump
    # print(ast.dump(node, include_attributes=True))
    # print(ast.dump(node.names[0], include_attributes=True))

    # Examples:
    # - `import altair`:
    # Import(names=[alias(name='altair', asname=None)], lineno=1, col_offset=0)
    # - `import altair as alt`:
    # Import(names=[alias(name='altair', asname='alt')], lineno=1, col_offset=0)

    for n in node.names:
        if n.name in name2asname and n.asname != name2asname[n.name]:
            errors.append((node.lineno, node.col_offset, name2message[n.name]))

    return errors


# @attr.s
@define
class Visitor(ast.NodeVisitor):
    # https://www.attrs.org/en/latest/names.html
    # https://www.attrs.org/en/latest/overview.html
    # errors: List[Tuple[int, int, str]] = attr.ib(factory=list)
    errors: List[Tuple[int, int, str]] = Factory(list)

    # More info: https://docs.python.org/3/library/ast.html#ast.Import
    # https://github.com/asottile/flake8-2020/blob/v1.7.0/flake8_2020.py#L36
    # https://docs.python.org/3/library/ast.html#ast.ImportFrom
    def visit_Import(self, node: ast.Import) -> None:
        # Called for `import ..` and `import .. as ..` nodes
        self.generic_visit(node)  # Continue checking children
        self.errors.extend(check_import_name(node))
