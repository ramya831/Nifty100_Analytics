import pandas as pd

print("Loading files...")

financial = pd.read_excel("data/raw/financial_ratios.xlsx")

peer = pd.read_excel("data/raw/peer_groups.xlsx")

# Read companies.xlsx using the SECOND row as column names
companies = pd.read_excel(
    "data/raw/companies.xlsx",
    header=1
)

print("\nCompanies Columns:")
print(companies.columns)

print("\nFirst 5 Companies:")
print(companies.head())