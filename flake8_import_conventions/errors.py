def generate_message(number: int, package_name: str, import_convention: str) -> str:
    pad_number = str(number).zfill(3)

    return f"IC{pad_number} {package_name} should be imported as `{import_convention}`"


IC001 = generate_message(1, "pandas", "import pandas as pd")
