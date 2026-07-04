from src.analytics.cashflow_kpis import *


def test_free_cash_flow():
    assert free_cash_flow(100, -40) == 60


def test_cfo_quality():
    assert cfo_quality_score(120, 100) == "High Quality"


def test_capex():
    assert capex_intensity(-50, 1000) == 5


def test_fcf_conversion():
    assert fcf_conversion_rate(60, 120) == 50


def test_pattern():
    assert capital_allocation_pattern(100, -50, -20) == "Reinvestor"