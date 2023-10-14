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
            "matplotlib.pyplot",
            "plt",
            "IC003 matplotlib.pyplot should be imported as `import matplotlib.pyplot as plt`",
        ),
        (
            4,
            "networkx",
            "nx",
            "IC004 networkx should be imported as `import networkx as nx`",
        ),
        (
            5,
            "numpy",
            "np",
            "IC005 numpy should be imported as `import numpy as np`",
        ),
        (
            6,
            "pandas",
            "pd",
            "IC006 pandas should be imported as `import pandas as pd`",
        ),
        (
            7,
            "plotly.express",
            "px",
            "IC007 plotly.express should be imported as `import plotly.express as px`",
        ),
        (
            8,
            "plotly.graph_objects",
            "go",
            "IC008 plotly.graph_objects should be imported as `import plotly.graph_objects as go`",
        ),
        (
            9,
            "seaborn",
            "sns",
            "IC009 seaborn should be imported as `import seaborn as sns`",
        ),
        (
            10,
            "statsmodels.api",
            "sm",
            "IC010 statsmodels.api should be imported as `import statsmodels.api as sm`",
        ),
        (
            11,
            "datetime",
            "dt",
            "IC011 datetime should be imported as `import datetime as dt`",
        ),
        (
            12,
            "tensorflow",
            "tf",
            "IC012 tensorflow should be imported as `import tensorflow as tf`",
        ),
        (
            13,
            "pickle",
            "pkl",
            "IC013 pickle should be imported as `import pickle as pkl`",
        ),
        (
            14,
            "multiprocessing",
            "mp",
            "IC014 multiprocessing should be imported as `import multiprocessing as mp`",
        )
    ],
)
def test_generate_message(number, package_number, alias, expected):
    assert generate_message(number, package_number, alias) == expected
