import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data ONCE
df = pd.read_csv("data/shl_catalog.csv")
df["combined_text"] = df["assessment_name"] + " " + df["skills"]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["combined_text"])

def recommend_assessments(text, top_n=5):
    query_vec = vectorizer.transform([text])
    scores = cosine_similarity(query_vec, X)[0]

    result_df = df.copy()
    result_df["score"] = scores

    top = result_df.sort_values("score", ascending=False).head(top_n)

    return {
        "recommendations": top[
            ["assessment_name", "assessment_type", "skills"]
        ].to_dict(orient="records"),
        "evaluation_metrics": {
            "avg_similarity": float(np.mean(top["score"]))
        }
    }