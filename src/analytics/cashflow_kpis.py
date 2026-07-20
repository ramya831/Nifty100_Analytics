import pandas as pd


def cfo_quality(cfo, pat):

    if pat == 0:
        return 0, "Unknown"

    score = cfo / pat

    if score > 1:
        label = "High Quality"
    elif score >= 0.5:
        label = "Moderate"
    else:
        label = "Accrual Risk"

    return round(score, 2), label


def capex_intensity(investing, sales):

    if sales == 0:
        return 0, "Unknown"

    value = abs(investing) / sales * 100

    if value < 3:
        label = "Asset Light"
    elif value <= 8:
        label = "Moderate"
    else:
        label = "Capital Intensive"

    return round(value, 2), label


def distress_signal(cfo, cff):

    return cfo < 0 and cff > 0


def deleveraging(cff, borrowings_old, borrowings_new):

    return cff < 0 and borrowings_new < borrowings_old