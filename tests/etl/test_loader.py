import pytest
from src.etl.loader import make_unique


def test_make_unique_no_duplicates():
    cols = ["id", "name", "price"]
    assert make_unique(cols) == ["id", "name", "price"]


def test_make_unique_one_duplicate():
    cols = ["price", "price"]
    assert make_unique(cols) == ["price", "price_1"]


def test_make_unique_multiple_duplicates():
    cols = ["year", "year", "year"]
    assert make_unique(cols) == [
        "year",
        "year_1",
        "year_2"
    ]


def test_make_unique_spaces():
    cols = [" id ", " name "]
    assert make_unique(cols) == [
        "id",
        "name"
    ]


def test_make_unique_empty():
    cols = []
    assert make_unique(cols) == []


def test_make_unique_numbers():
    cols = [1, 1, 2]
    assert make_unique(cols) == [
        "1",
        "1_1",
        "2"
    ]


def test_make_unique_mixed():
    cols = ["A", "A", "B", "B"]
    assert make_unique(cols) == [
        "A",
        "A_1",
        "B",
        "B_1"
    ]


def test_make_unique_case_sensitive():
    cols = ["Price", "price"]
    assert make_unique(cols) == [
        "Price",
        "price"
    ]


def test_make_unique_many():
    cols = ["A"] * 5
    assert make_unique(cols) == [
        "A",
        "A_1",
        "A_2",
        "A_3",
        "A_4"
    ]


def test_make_unique_strings():
    cols = ["roe", "roe", "roce"]
    result = make_unique(cols)

    assert isinstance(result, list)
    assert len(result) == 3