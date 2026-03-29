from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="ML Regression API")

# Allow requests from GitHub Pages (and anywhere during dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once on startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


class PredictRequest(BaseModel):
    features: list[float]  # expects [f1, f2, f3, f4, f5]


class PredictResponse(BaseModel):
    prediction: float


@app.get("/")
def root():
    return {"status": "ML API is running ✅"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    data = np.array([request.features])
    prediction = model.predict(data)[0]
    return {"prediction": float(prediction)}
