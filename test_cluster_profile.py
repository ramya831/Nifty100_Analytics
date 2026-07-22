import pandas as pd

from src.analytics.cluster_profile import create_cluster_profile

# ---------------------------------
# Sample Data
# ---------------------------------

companies = pd.DataFrame({

    "company_id":[1,2,3,4,5],

    "cluster_name":[
        "Emerging Growth",
        "High Quality Compounders",
        "Value Cyclicals",
        "Distressed Turnaround",
        "Defensive Dividend Payers"
    ],

    "return_on_equity_pct":[18,32,14,4,20],

    "debt_to_equity":[0.5,0.2,1.4,3.2,0.4],

    "revenue_cagr_5yr":[15,24,8,2,10],

    "fcf_cagr_5yr":[12,21,6,-5,8],

    "operating_profit_margin_pct":[18,30,12,5,20]

})

mean_df, median_df, outliers, stats = create_cluster_profile(companies)

print("\nCluster Mean\n")
print(mean_df)

print("\nCluster Median\n")
print(median_df)

print("\nOutliers\n")
print(outliers)

print("\nPortfolio Statistics\n")
print(stats)