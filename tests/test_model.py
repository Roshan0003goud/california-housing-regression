import joblib
import numpy as np


def test_model_loads():
    model = joblib.load('models/final_model.pkl')
    assert model is not None

def test_model_predicts():
    model = joblib.load('models/final_model.pkl')
    scaler = joblib.load('data/scaler.pkl')
    
    sample = np.array([[5.0, 30, 5.0, 1.0, 800, 2.5, 37.77, -122.4, 2.0, 0.2, 320.0, 2.4]])
    scaled = scaler.transform(sample)
    predictions = model.predict(scaled)
    
    
    assert predictions[0] > 0
    