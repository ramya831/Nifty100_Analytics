from src.reports.tearsheet import generate_tearsheet

companies = [
    "TCS",
    "INFY",
    "HDFCBANK",
    "RELIANCE",
    "ICICIBANK",
    "HINDUNILVR",
    "ITC",
    "LT",
    "SBIN",
    "SUNPHARMA"
]

for company in companies:
    generate_tearsheet(company)
    print(f"{company} PDF Generated")

print("\nBatch Generation Completed")