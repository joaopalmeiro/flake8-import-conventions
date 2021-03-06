import ast

import pytest

from flake8_import_conventions import Plugin


def results(s):
    # Based on:
    # - https://github.com/asottile/flake8-2020/blob/master/tests/flake8_2020_test.py

    # lineno: starts at 1.
    # col_offset: starts at 0.
    return {"{}:{}: {}".format(*r) for r in Plugin(ast.parse(s)).run()}


@pytest.mark.parametrize(
    "s",
    (
        "",
        "import altair as alt",
        "import numpy as np",
        "import pandas as pd",
        "import seaborn as sns",
    ),
)
def test_ok(s):
    assert results(s) == set()


# Altair
@pytest.mark.parametrize(
    "s",
    ("import altair", "import altair as altt", "import altair as Alt"),
)
def test_import_altair(s):
    assert results(s) == {
        "1:0: IC001 altair should be imported as `import altair as alt`"
    }


# NumPy
@pytest.mark.parametrize(
    "s",
    ("import numpy", "import numpy as npp", "import numpy as Np"),
)
def test_import_numpy(s):
    assert results(s) == {"1:0: IC002 numpy should be imported as `import numpy as np`"}


# pandas
@pytest.mark.parametrize(
    "s",
    ("import pandas", "import pandas as pdd", "import pandas as Pd"),
)
def test_import_pandas(s):
    assert results(s) == {
        "1:0: IC003 pandas should be imported as `import pandas as pd`"
    }


# Seaborn
@pytest.mark.parametrize(
    "s",
    ("import seaborn", "import seaborn as snss", "import seaborn as Sns"),
)
def test_import_seaborn(s):
    assert results(s) == {
        "1:0: IC004 seaborn should be imported as `import seaborn as sns`"
    }
