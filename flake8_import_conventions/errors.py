from typing import Dict, Optional


def generate_code(number: int) -> str:
    pad_number = str(number).zfill(3)

    return f"IC{pad_number}"


def generate_description(package_name: str, alias: Optional[str]) -> str:
    import_convention = (
        f"import {package_name} as {alias}" if alias else f"import {package_name}"
    )

    return f"{package_name} should be imported as `{import_convention}`"


def generate_message(number: int, package_name: str, alias: Optional[str]) -> str:
    code = generate_code(number)
    description = generate_description(package_name, alias)

    return f"{code} {description}"


# https://github.com/charliermarsh/ruff/blob/v0.0.241/src/rules/flake8_import_conventions/settings.rs
# https://github.com/geopandas/geopandas/issues/716
# Alphabetical order:
name2asname: Dict[str, Optional[str]] = {
    "altair": "alt",
    "geopandas": None,
    "matplotlib.pyplot": "plt",
    "networkx": "nx",
    "numpy": "np",
    "pandas": "pd",
    "plotly.express": "px",
    "plotly.graph_objects": "go",
    "seaborn": "sns",
}

name2message: Dict[str, str] = {
    key: generate_message(idx + 1, key, value)
    for idx, (key, value) in enumerate(name2asname.items())
}
