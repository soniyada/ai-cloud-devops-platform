from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.model import predict_sentiment

app = FastAPI(
    title="AI Cloud Platform",
    description="A machine-learning sentiment analysis API",
    version="1.0.0",
)


class PredictionRequest(BaseModel):
    text: str = Field(min_length=2, max_length=1000)


@app.get("/")
def home():
    return {
        "message": "AI Cloud Platform is running",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(request: PredictionRequest):
    return {
        "text": request.text,
        "sentiment": predict_sentiment(request.text),
    }
