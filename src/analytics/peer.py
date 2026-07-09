import os
import sqlite3
import pandas as pd

print("Peer Ranking Started...")

# -----------------------------
# Load Data
# -----------------------------
financial = pd.read_excel("data/raw/financial_ratios.xlsx")
peer = pd.read_excel("data/raw/peer_groups.xlsx")

# Merge
merged = financial.merge(
    peer,
    on="company_id",
    how="left"
)

# -----------------------------
# Metrics available in your dataset
# -----------------------------
metrics = [
    "return_on_equity_pct",
    "net_profit_margin_pct",
    "debt_to_equity",
    "interest_coverage",
    "asset_turnover",
    "free_cash_flow_cr"
]

results = []

print("\nCalculating Percentile Rankings...")

# -----------------------------
# Calculate Percentiles
# -----------------------------
for group_name, group in merged.groupby("peer_group_name"):

    if pd.isna(group_name):
        continue

    temp = group.copy()

    for metric in metrics:

        if metric not in temp.columns:
            continue

        if metric == "debt_to_equity":
            temp[f"{metric}_percentile"] = (
                1 - temp[metric].rank(pct=True)
            ) * 100
        else:
            temp[f"{metric}_percentile"] = (
                temp[metric].rank(pct=True)
            ) * 100

    results.append(temp)

# -----------------------------
# Combine Results
# -----------------------------
peer_df = pd.concat(results, ignore_index=True)

# -----------------------------
# Save Excel
# -----------------------------
os.makedirs("output", exist_ok=True)

excel_path = "output/peer_comparison.xlsx"

with pd.ExcelWriter(excel_path) as writer:

    for group_name, group in peer_df.groupby("peer_group_name"):

        group.to_excel(
            writer,
            sheet_name=str(group_name)[:31],
            index=False
        )

print("\nExcel File Created!")
print(excel_path)

# -----------------------------
# Save SQLite
# -----------------------------
db_path = "data/nifty100.db"

conn = sqlite3.connect(db_path)

peer_df.to_sql(
    "peer_percentiles",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nSQLite Table Created!")
print("Table Name : peer_percentiles")

print("\nDay 20 Completed Successfully!")