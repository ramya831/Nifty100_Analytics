from src.reports.sector_report import generate_sector_report

companies = [
    {"Company": "TCS", "ROE": 25, "Revenue": 220000},
    {"Company": "Infosys", "ROE": 22, "Revenue": 180000},
    {"Company": "Wipro", "ROE": 18, "Revenue": 120000},
    {"Company": "HCL", "ROE": 20, "Revenue": 150000},
]

generate_sector_report("IT", companies)

print("Sector Report Generated Successfully!")