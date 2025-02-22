from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy as np

app = FastAPI()

# Define input model with corrected field names
class ModelInput(BaseModel):
    pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float  # ✅ Fixed spelling
    Age: int

# Load the saved model
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
except FileNotFoundError:
    raise Exception("Model file 'diabetes_model.sav' not found!")

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters: ModelInput):
    # Convert input to dictionary
    input_dict = input_parameters.dict()
    
    # Extract values correctly
    input_list = [
        input_dict['pregnancies'],
        input_dict['Glucose'],
        input_dict['BloodPressure'],
        input_dict['SkinThickness'],
        input_dict['Insulin'],
        input_dict['BMI'],  # ✅ Fixed from 'BMT'
        input_dict['DiabetesPedigreeFunction'],  # ✅ Fixed spelling
        input_dict['Age']
    ]

    # Convert input to NumPy array and make prediction
    input_array = np.array([input_list])
    prediction = diabetes_model.predict(input_array)

    # Return result
    return {"prediction": "Diabetic" if prediction[0] == 1 else "Not Diabetic"}
