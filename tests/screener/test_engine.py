import pandas as pd

from src.screener.engine import apply_filters


def test_filter():

    df = pd.DataFrame({
        "ROE": [10, 18, 25],
        "composite_quality_score": [50, 80, 90]
    })

    filters = {
        "ROE": 15
    }

    result = apply_filters(df, filters)

    assert len(result) == 2