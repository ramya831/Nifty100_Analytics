import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore


def create_cluster_profile(df):
    """
    Generate cluster statistics, heatmap, outlier report,
    and portfolio statistics.
    """

    # -----------------------------
    # Create folders if not exist
    # -----------------------------
    os.makedirs("output", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    # -----------------------------
    # Numeric columns only
    # -----------------------------
    numeric_columns = [
        "return_on_equity_pct",
        "debt_to_equity",
        "revenue_cagr_5yr",
        "fcf_cagr_5yr",
        "operating_profit_margin_pct"
    ]

    # -----------------------------
    # Cluster Mean
    # -----------------------------
    cluster_mean = (
        df.groupby("cluster_name")[numeric_columns]
        .mean()
        .round(2)
    )

    cluster_mean.to_csv(
        "output/cluster_mean.csv"
    )

    # -----------------------------
    # Cluster Median
    # -----------------------------
    cluster_median = (
        df.groupby("cluster_name")[numeric_columns]
        .median()
        .round(2)
    )

    cluster_median.to_csv(
        "output/cluster_median.csv"
    )

    # -----------------------------
    # Correlation Heatmap
    # -----------------------------
    corr = df[numeric_columns].corr()

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(
        "reports/correlation_heatmap.png"
    )

    plt.close()

    # -----------------------------
    # Outlier Detection
    # -----------------------------
    z_scores = df[numeric_columns].apply(zscore)

    outliers = df[
        (z_scores.abs() > 3).any(axis=1)
    ]

    outliers.to_csv(
        "output/outlier_report.csv",
        index=False
    )

    # -----------------------------
    # Portfolio Statistics
    # -----------------------------
    stats = pd.DataFrame(index=numeric_columns)

    stats["Mean"] = df[numeric_columns].mean()
    stats["Std"] = df[numeric_columns].std()
    stats["P10"] = df[numeric_columns].quantile(0.10)
    stats["P25"] = df[numeric_columns].quantile(0.25)
    stats["P50"] = df[numeric_columns].quantile(0.50)
    stats["P75"] = df[numeric_columns].quantile(0.75)
    stats["P90"] = df[numeric_columns].quantile(0.90)

    stats = stats.round(2)

    stats.to_csv(
        "output/portfolio_stats.csv"
    )

    print("\nCluster profiling completed successfully.\n")

    return (
        cluster_mean,
        cluster_median,
        outliers,
        stats
    )