import pandas as pd
import yaml


def load_config(config_path):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def apply_filters(df, filters):

    filtered = df.copy()

    for column, value in filters.items():

        if column not in filtered.columns:
            continue

        filtered = filtered[filtered[column] >= value]

    if "composite_quality_score" in filtered.columns:
        filtered = filtered.sort_values(
            by="composite_quality_score",
            ascending=False
        )

    return filtered