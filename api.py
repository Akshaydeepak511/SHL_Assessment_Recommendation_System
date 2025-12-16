from fastapi import FastAPI
from pydantic import BaseModel
from recommender import recommend_assessments

app = FastAPI()

class RequestBody(BaseModel):
    input: str
    type: str

@app.post("/recommend")
def recommend(body: RequestBody):
    return recommend_assessments(body.input)