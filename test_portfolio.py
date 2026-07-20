from src.reports.portfolio_summary import generate_portfolio_summary

companies = [

    {
        "Ticker":"TCS",
        "Sector":"IT",
        "ROE":25,
        "Revenue CAGR":15,
        "DE":0.18,
        "FCF":5.2,
        "PE":28
    },

    {
        "Ticker":"INFY",
        "Sector":"IT",
        "ROE":22,
        "Revenue CAGR":14,
        "DE":0.10,
        "FCF":4.8,
        "PE":26
    },

    {
        "Ticker":"RELIANCE",
        "Sector":"Energy",
        "ROE":18,
        "Revenue CAGR":11,
        "DE":0.42,
        "FCF":3.4,
        "PE":24
    }

]

generate_portfolio_summary(companies)