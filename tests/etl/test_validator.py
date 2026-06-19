import pandas as pd

from etl.validator import (
    check_positive_sales
)


def test_negative_sales():

    df = pd.DataFrame({
        "sales":[100,-50,200]
    })

    result = check_positive_sales(df)

    assert len(result)==1