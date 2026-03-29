from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pickle
import numpy as np

app = FastAPI(title="Student Performance Predictor API")

# Allow requests from GitHub Pages frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once on startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


class StudentInput(BaseModel):
    iq:                   float = Field(..., ge=0, le=10, description="IQ Score (0-10)")
    cgpa:                 float = Field(..., ge=0, le=10, description="CGPA (0-10)")
    marks_10th:           float = Field(..., ge=0, le=10, description="10th Marks (0-10)")
    marks_12th:           float = Field(..., ge=0, le=10, description="12th Marks (0-10)")
    communication_skills: float = Field(..., ge=0, le=10, description="Communication Skills (0-10)")


class PredictionOutput(BaseModel):
    prediction: float


@app.get("/")
def root():
    return {"status": "Student Performance Predictor API is running ✅"}


@app.post("/predict", response_model=PredictionOutput)
def predict(data: StudentInput):
    features = np.array([[
        data.iq,
        data.cgpa,
        data.marks_10th,
        data.marks_12th,
        data.communication_skills
    ]])
    prediction = model.predict(features)[0]
    return {"prediction": round(float(prediction), 4)}
