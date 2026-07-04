from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    debt_to_equity,
    high_leverage_flag,
    interest_coverage,
    interest_coverage_label,
    interest_warning_flag,
    net_debt,
    asset_turnover,
)


# -----------------------------
# Day 08 Tests
# -----------------------------

def test_net_profit_margin():
    assert net_profit_margin(100, 1000) == 10


def test_zero_sales():
    assert net_profit_margin(100, 0) is None


def test_operating_profit_margin():
    assert operating_profit_margin(200, 1000) == 20


def test_return_on_equity():
    assert return_on_equity(100, 500, 500) == 10


def test_negative_equity():
    assert return_on_equity(100, -500, -500) is None


def test_return_on_capital():
    assert return_on_capital_employed(100, 500, 500, 1000) == 5


def test_return_on_assets():
    assert return_on_assets(100, 1000) == 10


def test_zero_assets():
    assert return_on_assets(100, 0) is None


# -----------------------------
# Day 09 Tests
# -----------------------------

def test_debt_to_equity():
    assert debt_to_equity(100, 500, 500) == 0.1


def test_debt_free():
    assert debt_to_equity(0, 500, 500) == 0


def test_high_leverage():
    assert high_leverage_flag(6, "Technology") is True


def test_financial_sector():
    assert high_leverage_flag(8, "Financials") is False


def test_interest_coverage():
    assert interest_coverage(100, 20, 10) == 12


def test_icr_zero_interest():
    assert interest_coverage(100, 20, 0) is None


def test_debt_free_label():
    assert interest_coverage_label(None) == "Debt Free"


def test_interest_warning():
    assert interest_warning_flag(1) is True


def test_net_debt():
    assert net_debt(500, 100) == 400


def test_asset_turnover():
    assert asset_turnover(1000, 500) == 2


def test_zero_asset_turnover():
    assert asset_turnover(1000, 0) is None
    
import os
from src.analytics.ratios import save_financial_ratio


def test_save_ratio():
    db = "test_ratios.db"

    save_financial_ratio(
        db,
        1,
        2024,
        "ROE",
        15.5
    )

    assert os.path.exists(db)

    os.remove(db)