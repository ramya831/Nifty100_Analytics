from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
)


def test_net_profit_margin():
    assert net_profit_margin(100, 1000) == 10


def test_zero_sales():
    assert net_profit_margin(100, 0) is None


def test_operating_profit_margin():
    assert operating_profit_margin(200, 1000) == 20


def test_return_on_equity():
    assert return_on_equity(100, 500, 500) == 10


def test_negative_equity():
    assert return_on_equity(100, -500, 100) is None


def test_return_on_capital_employed():
    assert return_on_capital_employed(200, 500, 500, 1000) == 10


def test_return_on_assets():
    assert return_on_assets(100, 1000) == 10


def test_zero_assets():
    assert return_on_assets(100, 0) is None