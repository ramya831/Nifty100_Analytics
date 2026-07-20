import pandas as pd

from src.nlp.pros_cons_generator import generate_pros_cons

data = {

    "company_id": [1, 2],

    "ROE": [25, 8],

    "ROCE": [28, 6],

    "FCF": [5000, -200],

    "Debt_Equity": [0.4, 3.2],

    "Revenue_CAGR": [18, 2]

}

df = pd.DataFrame(data)

result = generate_pros_cons(df)

print(result)

result.to_csv(
    "output/pros_cons_generated.csv",
    index=False
)