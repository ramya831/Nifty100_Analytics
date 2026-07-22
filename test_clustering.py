import pandas as pd

from src.analytics.clustering import run_clustering

companies = pd.DataFrame({

    "company_id":[1,2,3,4,5],

    "company_name":[
        "TCS",
        "INFY",
        "RELIANCE",
        "ITC",
        "TATASTEEL"
    ],

    "return_on_equity_pct":[25,22,18,20,8],

    "debt_to_equity":[0.1,0.2,0.5,0.3,1.4],

    "revenue_cagr_5yr":[15,14,11,8,3],

    "fcf_cagr_5yr":[18,16,10,6,1],

    "operating_profit_margin_pct":[28,27,18,22,7]

})

result = run_clustering(companies)

print(result)

result[
    [
        "company_id",
        "cluster_id",
        "cluster_name",
        "distance_from_centroid"
    ]
].to_csv(
    "output/cluster_labels.csv",
    index=False
)