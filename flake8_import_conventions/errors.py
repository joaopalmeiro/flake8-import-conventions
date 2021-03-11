from typing import Dict


def generate_message(number: int, package_name: str, alias: str) -> str:
    pad_number = str(number).zfill(3)
    import_convention = f"import {package_name} as {alias}"

    return f"IC{pad_number} {package_name} should be imported as `{import_convention}`."


name_asname: Dict[str, str] = {"pandas": "pd"}

name_message: Dict[str, str] = {
    key: generate_message(idx + 1, key, value)
    for idx, (key, value) in enumerate(name_asname.items())
}
