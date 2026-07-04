def calculate_cagr(start, end, years):
    """
    Calculate CAGR (Compound Annual Growth Rate)
    """

    if years <= 0:
        return None, "INVALID_PERIOD"

    if start == 0:
        return None, "ZERO_BASE"

    if start > 0 and end > 0:
        cagr = ((end / start) ** (1 / years) - 1) * 100
        return round(cagr, 2), "NORMAL"

    if start > 0 and end < 0:
        return None, "DECLINE_TO_LOSS"

    if start < 0 and end > 0:
        return None, "TURNAROUND"

    if start < 0 and end < 0:
        return None, "BOTH_NEGATIVE"

    return None, "INSUFFICIENT"