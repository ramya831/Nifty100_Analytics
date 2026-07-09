import os
import numpy as np
import matplotlib.pyplot as plt

# Create folder
os.makedirs("reports/radar_charts", exist_ok=True)

# Companies
companies = [
    "ABB",
    "TCS",
    "INFY",
    "HDFCBANK",
    "RELIANCE"
]

# Metrics
labels = [
    "ROE",
    "ROCE",
    "NPM",
    "D/E",
    "FCF",
    "PAT CAGR",
    "Revenue CAGR",
    "Composite"
]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

for company in companies:

    # Random values (temporary)
    company_values = np.random.randint(60, 95, len(labels)).tolist()
    peer_values = np.random.randint(50, 85, len(labels)).tolist()

    company_values += company_values[:1]
    peer_values += peer_values[:1]

    plt.figure(figsize=(8,8))

    ax = plt.subplot(111, polar=True)

    ax.plot(angles, company_values, linewidth=2, label=company)
    ax.fill(angles, company_values, alpha=0.25)

    ax.plot(
        angles,
        peer_values,
        linewidth=2,
        linestyle="--",
        label="Peer Average"
    )

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title(f"{company} Peer Comparison")

    plt.legend(loc="upper right")

    plt.savefig(
        f"reports/radar_charts/{company}_radar.png",
        dpi=300
    )

    plt.close()

print("\nAll Radar Charts Generated Successfully!")