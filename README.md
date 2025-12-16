# SHL_Assessment_Recommendation_System
This project implements an intelligent SHL assessment recommendation system using NLP and similarity-based ranking, with built-in evaluation metrics to measure accuracy and effectiveness.
1️⃣ Prerequisites
Ensure the following are installed on your system:
Python 3.9 or above
Git
Internet connection (for JD URL parsing)
Verify Python installation: python --version
2️⃣ Clone the Repository
git clone <your-github-repo-url>
cd SHL_Assessment_Recommendation_System_With_Metrics
3️⃣ Create Virtual Environment
python -m venv venv
Activate the virtual environment:
venv\Scripts\activate
If activated successfully, (venv) will appear in the terminal.
4️⃣ Install Dependencies
Upgrade pip:
python -m pip install --upgrade pip
Install required libraries:
python -m pip install -r requirements.txt
5️⃣ Start Backend API (FastAPI)
uvicorn api:app --reload
Backend will start at:
http://localhost:8000
You should see:
Application startup complete
6️⃣ Start Frontend Web App (Streamlit)
Open a new terminal, activate the environment again:
venv\Scripts\activate
Run the Streamlit app:
streamlit run app.py
Web application will open at:
http://localhost:8501
7️⃣ Using the Application
Input Types Supported:
Natural Language Query
Job Description Text
Job Description URL
Example Input:
Looking for a Java developer with strong problem-solving skills
Click Get Recommendations to view:
Recommended SHL assessments
Evaluation metrics (Precision@5, Recall@5, Similarity Score)

Author:
Email : akshaydeepak511@gmail.com
LinkedIn : T M AKSHAY DEEPAK
