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
            "geopandas",
            None,
            "IC002 geopandas should be imported as `import geopandas`",
        ),
        (
            3,
            "numpy",
            "np",
            "IC003 numpy should be imported as `import numpy as np`",
        ),
        (
            4,
            "pandas",
            "pd",
            "IC004 pandas should be imported as `import pandas as pd`",
        ),
        (
            5,
            "plotly.express",
            "px",
            "IC005 plotly.express should be imported as `import plotly.express as px`",
        ),
        (
            6,
            "plotly.graph_objects",
            "go",
            "IC006 plotly.graph_objects should be imported as `import plotly.graph_objects as go`",
        ),
        (
            7,
            "seaborn",
            "sns",
            "IC007 seaborn should be imported as `import seaborn as sns`",
        ),
    ],
)
def test_generate_message(number, package_number, alias, expected):
    assert generate_message(number, package_number, alias) == expected
