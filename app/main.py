from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.schemas import NewsInput, PredictionOutput
from app.model_utils import make_prediction
import os

app = FastAPI(title="Fake News Detection Service")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    # Return the HTML file 
    return FileResponse(os.path.join("static", "index.html"))

@app.post("/predict", response_model=PredictionOutput)
def predict_news(payload: NewsInput):
    label, prob = make_prediction(payload.text)
    return {
        "prediction": label,
        "confidence": round(prob, 4)
    }