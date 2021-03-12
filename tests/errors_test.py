import pytest

from flake8_import_conventions.errors import generate_message


@pytest.mark.parametrize(
    "number,package_number,alias,expected",
    [
        (
            1,
            "altair",
            "alt",
            "IC001 altair should be imported as `import altair as alt`",
        ),
        (
            2,
            "numpy",
            "np",
            "IC002 numpy should be imported as `import numpy as np`",
        ),
        (
            3,
            "pandas",
            "pd",
            "IC003 pandas should be imported as `import pandas as pd`",
        ),
        (
            4,
            "seaborn",
            "sns",
            "IC004 seaborn should be imported as `import seaborn as sns`",
        ),
    ],
)
def test_generate_message(number, package_number, alias, expected):
    assert generate_message(number, package_number, alias) == expected
