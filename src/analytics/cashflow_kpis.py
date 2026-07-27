import pandas as pd


def free_cash_flow(cfo, capex):
    """Free Cash Flow = CFO + CapEx (CapEx is negative)."""
    return cfo + capex


def cfo_quality_score(cfo, pat):
    """Return CFO quality label."""
    if pat == 0:
        return "Unknown"

    score = cfo / pat

    if score >= 1:
        return "High Quality"
    elif score >= 0.5:
        return "Moderate"
    else:
        return "Accrual Risk"


def capex_intensity(investing, sales):
    """CapEx intensity percentage."""
    if sales == 0:
        return 0

    return round(abs(investing) / sales * 100, 2)


def fcf_conversion_rate(fcf, cfo):
    """FCF conversion percentage."""
    if cfo == 0:
        return 0

    return round((fcf / cfo) * 100, 2)


def capital_allocation_pattern(cfo, capex, dividends):
    """Simple capital allocation classification."""
    if cfo > 0 and capex < 0:
        return "Reinvestor"

    if dividends < 0:
        return "Dividend Payer"

    return "Balanced"


def distress_signal(cfo, cff):
    return cfo < 0 and cff > 0


def deleveraging(cff, borrowings_old, borrowings_new):
    return cff < 0 and borrowings_new < borrowings_old