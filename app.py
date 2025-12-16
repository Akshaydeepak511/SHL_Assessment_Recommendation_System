import streamlit as st
import requests

st.set_page_config(page_title="SHL Assessment Recommender")

st.title("🧠 SHL Assessment Recommendation System")

query_type = st.selectbox(
    "Select Input Type",
    ["Natural Language Query", "Job Description Text", "Job Description URL"]
)

user_input = st.text_area("Enter your input")

if st.button("Get Recommendations"):
    response = requests.post(
        "http://localhost:8000/recommend",
        json={"input": user_input, "type": query_type}
    )

    data = response.json()

    st.subheader("Recommended Assessments")
    for r in data["recommendations"]:
        st.markdown(f"**{r['assessment_name']}**")
        st.write(f"Type: {r['assessment_type']}")
        st.write(f"Skills: {r['skills']}")
        st.write("---")

    st.subheader("📊 Evaluation Metrics")
    st.metric("Precision@5", round(data["evaluation_metrics"]["precision@5"], 2))
    st.metric("Recall@5", round(data["evaluation_metrics"]["recall@5"], 2))
    st.metric("Avg Similarity Score", round(data["evaluation_metrics"]["avg_similarity@5"], 2))
