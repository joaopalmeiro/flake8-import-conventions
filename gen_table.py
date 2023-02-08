from typing import Dict

from tomark import Tomark

from flake8_import_conventions.errors import (
    generate_code,
    generate_description,
    name2asname,
)


def generate_link(text: str, url: str) -> str:
    return f"[{text}]({url})"


# Follow the same order as in name2asname:
name2stylized: Dict[str, str] = {
    "altair": "Altair",
    "geopandas": "GeoPandas",
    "matplotlib.pyplot": "Matplotlib",
    "networkx": "NetworkX",
    "numpy": "NumPy",
    "pandas": "pandas",
    "plotly.express": "Plotly",
    "plotly.graph_objects": "Plotly",
    "seaborn": "seaborn",
    "statsmodels.api": "statsmodels",
}
name2url: Dict[str, str] = {
    "altair": "https://altair-viz.github.io/",
    "geopandas": "https://geopandas.org/",
    "matplotlib.pyplot": "https://matplotlib.org/",
    "networkx": "https://networkx.org/",
    "numpy": "https://numpy.org/",
    "pandas": "https://pandas.pydata.org/",
    "plotly.express": "https://plotly.com/python/",
    "plotly.graph_objects": "https://plotly.com/python/",
    "seaborn": "https://seaborn.pydata.org/",
    "statsmodels.api": "https://www.statsmodels.org/",
}

if __name__ == "__main__":
    # Based on:
    # - https://github.com/queensferryme/flake8-too-many
    # - https://github.com/asottile/flake8-2020
    # - https://flake8.pycqa.org/en/latest/user/error-codes.html

    table_data = [
        {
            "Package": generate_link(name2stylized[key], name2url[key]),
            "Code": generate_code(idx),
            "Description": generate_description(key, value),
        }
        for idx, (key, value) in enumerate(name2asname.items(), start=1)
    ]

    # https://github.com/codazoda/tomark
    table_output = Tomark.table(table_data)
    print(table_output)
