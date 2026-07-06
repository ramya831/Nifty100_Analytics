import pandas as pd


def apply_filters(df, filters=None, **kwargs):
    result = df.copy()

    # Support tests like:
    # apply_filters(df, {"ROE": 15})
    if filters is not None:
        for column, value in filters.items():
            if column in result.columns:
                result = result[result[column] >= value]
        return result.reset_index(drop=True)

    # Support preset screeners
    if kwargs.get("roe_min") is not None:
        result = result[result["roe"] >= kwargs["roe_min"]]

    if kwargs.get("de_max") is not None:
        result = result[result["de"] <= kwargs["de_max"]]

    if kwargs.get("fcf_min") is not None:
        result = result[result["fcf"] >= kwargs["fcf_min"]]

    if kwargs.get("revenue_cagr_5yr_min") is not None:
        result = result[
            result["revenue_cagr_5yr"] >= kwargs["revenue_cagr_5yr_min"]
        ]

    if kwargs.get("pat_cagr_5yr_min") is not None:
        result = result[
            result["pat_cagr_5yr"] >= kwargs["pat_cagr_5yr_min"]
        ]

    if kwargs.get("pe_max") is not None:
        result = result[result["pe"] <= kwargs["pe_max"]]

    if kwargs.get("pb_max") is not None:
        result = result[result["pb"] <= kwargs["pb_max"]]

    if kwargs.get("dividend_yield_min") is not None:
        result = result[
            result["dividend_yield"] >= kwargs["dividend_yield_min"]
        ]

    if kwargs.get("dividend_payout_max") is not None:
        result = result[
            result["dividend_payout"] <= kwargs["dividend_payout_max"]
        ]

    if kwargs.get("sales_min") is not None:
        result = result[result["sales"] >= kwargs["sales_min"]]

    return result.reset_index(drop=True)

# -----------------------------
# Day 16 Presets
# -----------------------------

def quality_compounder(df):
    return apply_filters(
        df,
        roe_min=15,
        de_max=1,
        fcf_min=0,
        revenue_cagr_5yr_min=10,
    )


def value_pick(df):
    return apply_filters(
        df,
        pe_max=20,
        pb_max=3,
        de_max=2,
        dividend_yield_min=1,
    )


def growth_accelerator(df):
    return apply_filters(
        df,
        pat_cagr_5yr_min=20,
        revenue_cagr_5yr_min=15,
        de_max=2,
    )


def dividend_champion(df):
    return apply_filters(
        df,
        dividend_yield_min=2,
        dividend_payout_max=80,
        fcf_min=0,
    )


def debt_free_bluechip(df):
    return apply_filters(
        df,
        de_max=0,
        roe_min=12,
        sales_min=5000,
    )


def turnaround_watch(df):
    return apply_filters(
        df,
        revenue_cagr_5yr_min=10,
        fcf_min=0,
    )


PRESETS = {
    "Quality Compounder": quality_compounder,
    "Value Pick": value_pick,
    "Growth Accelerator": growth_accelerator,
    "Dividend Champion": dividend_champion,
    "Debt-Free Blue Chip": debt_free_bluechip,
    "Turnaround Watch": turnaround_watch,
}


def run_preset(df, preset_name):
    """
    Execute one of the predefined screeners.
    """
    if preset_name not in PRESETS:
        raise ValueError(f"Unknown preset: {preset_name}")

    return PRESETS[preset_name](df)