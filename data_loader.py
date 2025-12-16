import pandas as pd

def load_catalog():
    df = pd.read_csv("data/shl_catalog.csv")
    df["combined_text"] = df["assessment_name"] + " " + df["skills"]
    return df
