import joblib
import numpy as np
import pandas as pd
import geopandas as gpd
from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow import keras
from fastapi.middleware.cors import CORSMiddleware
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from joblib import load

from pydantic import BaseModel

model = keras.models.load_model('best_deep_model.keras')
preprocessor = load("preprocessor.joblib")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionRequest(BaseModel):
    terrain_area: float
    built_area: float
    offer: float
    zh: int

    

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/getPoints")
async def get_points():
    gdf = gpd.read_file("pontos.geojson")
    geojson = gdf.to_json()
    
    return geojson

@app.post("/newPrediction")
async def new_prediction(newPred: PredictionRequest):
    df = pd.DataFrame([{
        "at": newPred.terrain_area,
        "vc": newPred.built_area,
        "oferta": newPred.offer,
        "zh": newPred.zh
    }])

    X_processed = preprocessor.transform(df)

    pred = model.predict(X_processed).flatten()
    value = 10 ** pred -1

    return {
        "Valor predito": round(float(value),2)
    }
