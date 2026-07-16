import pandas as pd


def calculate_fcf_yield(fcf, market_cap):
    if market_cap <= 0:
        return None
    return round((fcf / market_cap) * 100, 2)


def get_valuation_flag(pe, sector_median):
    if pe > sector_median * 1.5:
        return "Caution"
    elif pe < sector_median * 0.7:
        return "Discount"
    else:
        return "Fair"


data = pd.DataFrame({
    "Company": ["TCS", "Infosys", "ITC", "Reliance"],
    "Sector": ["IT", "IT", "FMCG", "Energy"],
    "PE": [30, 24, 18, 22],
    "PB": [12, 9, 6, 2],
    "EV_EBITDA": [18, 16, 12, 10],
    "MarketCap": [1500, 1200, 800, 2000],
    "FCF": [120, 100, 60, 140]
})

sector_pe = {
    "IT": 27,
    "FMCG": 20,
    "Energy": 18
}

data["FCF_Yield"] = data.apply(
    lambda x: calculate_fcf_yield(
        x["FCF"],
        x["MarketCap"]
    ),
    axis=1
)

data["Sector_Median_PE"] = data["Sector"].map(sector_pe)

data["Flag"] = data.apply(
    lambda x: get_valuation_flag(
        x["PE"],
        x["Sector_Median_PE"]
    ),
    axis=1
)

data.to_excel(
    "output/valuation_summary.xlsx",
    index=False
)

data[data["Flag"] != "Fair"].to_csv(
    "output/valuation_flags.csv",
    index=False
)

print("Valuation reports generated successfully.")