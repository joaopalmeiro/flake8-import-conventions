from typing import Dict


def generate_code(number: int) -> str:
    pad_number = str(number).zfill(3)

    return f"IC{pad_number}"


def generate_description(package_name: str, alias: str) -> str:
    import_convention = f"import {package_name} as {alias}"

    return f"{package_name} should be imported as `{import_convention}`"


def generate_message(number: int, package_name: str, alias: str) -> str:
    code = generate_code(number)
    description = generate_description(package_name, alias)

    return f"{code} {description}"


# Alphabetical order
name2asname: Dict[str, str] = {
    "altair": "alt",
    "numpy": "np",
    "pandas": "pd",
    "seaborn": "sns",
}

name2message: Dict[str, str] = {
    key: generate_message(idx + 1, key, value)
    for idx, (key, value) in enumerate(name2asname.items())
}
