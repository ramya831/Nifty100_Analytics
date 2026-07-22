import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def run_clustering(df):
    """
    Run KMeans clustering on company financial metrics.
    """

    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Features used for clustering
    features = [
        "return_on_equity_pct",
        "debt_to_equity",
        "revenue_cagr_5yr",
        "fcf_cagr_5yr",
        "operating_profit_margin_pct"
    ]

    # Fill missing values with median
    imputer = SimpleImputer(strategy="median")
    X = imputer.fit_transform(df[features])

    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # -----------------------------
    # Elbow Plot
    # -----------------------------
    inertia = []

    # Number of clusters cannot exceed number of samples
    max_clusters = min(10, len(df))

    for k in range(2, max_clusters + 1):
        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)
        inertia.append(model.inertia_)

    plt.figure(figsize=(6, 4))
    plt.plot(range(2, max_clusters + 1), inertia, marker="o")
    plt.title("KMeans Elbow Plot")
    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")
    plt.grid(True)

    plt.savefig("reports/elbow_plot.png")
    plt.close()

    # -----------------------------
    # Final KMeans Model
    # -----------------------------
    n_clusters = min(5, len(df))

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    df["cluster_id"] = kmeans.fit_predict(X_scaled)

    # Distance from centroid
    distances = kmeans.transform(X_scaled)

    df["distance_from_centroid"] = [
        distances[i][cluster]
        for i, cluster in enumerate(df["cluster_id"])
    ]

    # Cluster names
    cluster_names = {
        0: "High Quality Compounders",
        1: "Defensive Dividend Payers",
        2: "Value Cyclicals",
        3: "Distressed Turnaround",
        4: "Emerging Growth"
    }

    df["cluster_name"] = df["cluster_id"].map(cluster_names)

    return df